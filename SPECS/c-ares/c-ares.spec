Summary:        A library that performs asynchronous DNS operations
Name:           c-ares
Version:        1.18.1
Release:        1%{?dist}
License:        MIT
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          System Environment/Libraries
URL:            https://c-ares.org/
Source0:        https://c-ares.org/download/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

%description
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package devel
Summary:        Development files for c-ares
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkg-config

%description devel
This package contains the header files and libraries needed to
compile applications or shared objects that use c-ares.

%prep
%autosetup
f=CHANGES ; iconv -f iso-8859-1 -t utf-8 $f -o $f.utf8 ; mv $f.utf8 $f

%build
autoreconf -if
%configure --enable-shared --disable-static \
           --disable-dependency-tracking
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/%{_libdir}/libcares.la

%check
make %{?_smp_mflags} check

%clean
rm -rf %{buildroot}


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%license LICENSE.md
%doc README.md README.msvc README.cares CHANGES NEWS
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/ares.h
%{_includedir}/ares_build.h
%{_includedir}/ares_dns.h
%{_includedir}/ares_rules.h
%{_includedir}/ares_version.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/libcares.pc
%{_mandir}/man3/ares_*

%changelog
*   Mon Nov 29 2021 Andrew Phelps <anphel@microsoft.com> 1.18.1-1
-   Update to version 1.18.1 to address CVE-2021-3672
-   Update URL domain

*   Mon Mar 15 2021 Nick Samson <nisamson@microsoft.com> 1.17.1-1
-   Removed %%sha line. Upgraded to 1.17.1 to address CVE-2020-8277.
-   License confirmed as MIT. Changed URLs to use HTTPS.

*   Sat May 09 2020 Nick Samson <nisamson@microsoft.com> 1.14.0-3
-   Added %%license line automatically

*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 1.14.0-2
-   Initial CBL-Mariner import from Photon (license: Apache2).

*   Fri Sep 21 2018 Sujay G <gsujay@vmware.com> 1.14.0-1
-   Bump c-ares version to 1.14.0

*   Fri Sep 29 2017 Dheeraj Shetty <dheerajs@vmware.com>  1.12.0-2
-   Fix for CVE-2017-1000381

*   Fri Apr 07 2017 Anish Swaminathan <anishs@vmware.com>  1.12.0-1
-   Upgrade to 1.12.0

*   Wed Oct 05 2016 Xiaolin Li <xiaolinl@vmware.com> 1.10.0-3
-   Apply patch for CVE-2016-5180.

*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 1.10.0-2
-   GA - Bump release of all rpms

*   Wed Feb 03 2016 Anish Swaminathan <anishs@vmware.com> 1.10.0-1
-   Initial version
