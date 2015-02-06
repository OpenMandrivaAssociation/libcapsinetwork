%define major	0
%define libname %mklibname capsinetwork
%define develname %mklibname -d capsinetwork

Summary:	Network library for easy development of C++ server daemons
Name:		libcapsinetwork
Version:	0.3.0
Release:	7
License:	LGPL
Group:		System/Libraries
URL:		http://unixcode.org/libcapsinetwork/
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		libcapsinetwork-gcc43-includes.patch
BuildRequires:	automake

%description
%{name} is a network library for C++ server daemons aimed at easy
development of server daemons.

%package	-n %{libname}%{major}
Summary:	Network library for easy development of C++ server daemons
Group:		System/Libraries
Provides:	%{libname} = %{version}-%{release}

%description	-n %{libname}%{major}
%{name} is a network library for C++ server daemons aimed at easy
development of server daemons.


%package	-n %{develname}
Summary:	Development related files for %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname}-devel = %{version}-%{release}
Requires:	%{libname}%{major} = %{version}-%{release}
Obsoletes:	%{libname}%{major}-devel

%description	-n %{develname}
%{name} is a network library for C++ server daemons aimed at easy
development of server daemons.

You need to install this package if you want to develop or compile
any applications/libraries that needs %{name}.

%prep
%setup -q
%patch0 -p1 -b .gcc43

%build
libtoolize --force --copy
aclocal
autoheader
autoconf
automake -a -c
%configure2_5x --disable-static
# parallel build won't work
make

%install
%makeinstall_std

%files -n %{libname}%{major}
%doc COPYING.LIB README
%{_libdir}/lib*.so.*

%files -n %{develname}
%doc ChangeLog NEWS
%{_includedir}/*
%{_libdir}/lib*.so


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.0-5mdv2011.0
+ Revision: 620085
- the mass rebuild of 2010.0 packages

* Tue Jun 16 2009 Jérôme Brenier <incubusss@mandriva.org> 0.3.0-4mdv2010.0
+ Revision: 386417
- fix gcc43 patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jun 30 2007 Funda Wang <fwang@mandriva.org> 0.3.0-1mdv2008.0
+ Revision: 45999
- BR automake
- Add patch from debian to get it build on gcc 4.3
  use autotools
- New version
- Import libcapsinetwork



* Wed Jun 09 2004 Abel Cheung <deaddog@deaddog.org> 0.2.5-2mdk
- Rebuild with new gcc

* Wed Jan 28 2004 Abel Cheung <deaddog@deaddog.org> 0.2.5-1mdk
- First Mandrake package
