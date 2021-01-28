Name:          mobile-broadband-provider-info
Version:       20201225
Release:       1
Summary:       Mobile broadband provider database
License:       Public Domain
URL:           https://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
Source0:       https://ftp.gnome.org/pub/gnome/sources/mobile-broadband-provider-info/%{version}/%{name}-%{version}.tar.xz

BuildRequires: libxml2 /usr/bin/xsltproc /usr/bin/xmllint
BuildArch:     noarch

%description
This package contains mobile broadband settings for different service providers
in different countries. The Package contains only informational files so it's
safe for distributions to grab updates even during feature freeze and
maintenance stages.

%package devel
Summary:       Development package for mobile-broadband-provider-info
Requires:      %{name} = %{version}-%{release}

%description devel
The Development package for mobile-broadband-provider-info.

%package_help


%prep
%autosetup -n %{name}-%{version}

%build
%configure
%make_build

%check
make check

%install
%make_install


%files
%defattr(-,root,root)
%license COPYING
%{_datadir}/%{name}/*

%files devel
%{_datadir}/pkgconfig/%{name}.pc

%files help
%doc README

%changelog
* Thu Jan 28 2021 hanhui <hanhui15@huawei.com> - 20201225-1
- Type: enhancement
- ID:   NA
- SUG:  NA
- DESC: update to 20201225

* Mon Jul 27 2020 openEuler Buildteam <buildteam@openeuler.org> - 20190618-1
- Type: enhancement
- ID:   NA
- SUG:  NA
- DESC: Update to 20190618, add help package.

- Type: enhancement
- ID:   NA
- SUG:  NA
- DESC: Update to 20190116, add help package.

* Mon Aug 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 20170310-3
- Package init
