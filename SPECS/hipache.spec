
Name:          hipache
Version:       0.0.1
Release:       2%{?dist}
Summary:       a distributed HTTP and websocket proxy
Packager:      Aleksey Mykhailov <aleksey@myinvisible.net>
Group:         System Environment/Daemons
License:       MIT License
URL:           http://https://github.com/dotcloud/hipache
Source0:       %{name}-%{version}.tar.gz
Source1:       hipache.init
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root
requires:      nodejs >= 0.6.13-1
Patch0:	       app.pidfile.patch
Patch1:	       config.pidfile.patch


%description
Hipache is a distributed proxy designed to route high volumes of http and websocket traffic to unusually large numbers of virtual hosts

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/%{name}
cp -r * $RPM_BUILD_ROOT/opt/%{name}
# install SYSV init stuff
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m755 $RPM_SOURCE_DIR/hipache.init \
        $RPM_BUILD_ROOT/etc/rc.d/init.d/hipache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc /opt/%{name}/AUTHORS 
%doc /opt/%{name}/LICENSE
%doc /opt/%{name}/README.md
%doc /opt/%{name}/TODO.md
%dir /opt/%{name}
%config(noreplace) /opt/%{name}/config.json
%config(noreplace) /opt/%{name}/config_dev.json
%config(noreplace) /opt/%{name}/config_test.json
/opt/%{name}/app.js
/opt/%{name}/package.json
/opt/%{name}/lib/*
/opt/%{name}/static/*
/opt/%{name}/test/*
/opt/%{name}/node_modules/.bin/*
/opt/%{name}/node_modules/*
%{_sysconfdir}/rc.d/init.d/hipache

%changelog
* Tue Aug 14 2012 Aleksey Mykhailov
- Include required nodejs modules in package

* Mon Aug 13 2012 Aleksey Mykhailov
- First hipache package
