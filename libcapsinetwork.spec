%define	version	0.3.0
%define release	%mkrel 1

%define major	0
%define libname %mklibname capsinetwork
%define develname %mklibname -d capsinetwork

Summary:	Network library for easy development of C++ server daemons
Name:		libcapsinetwork
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Libraries
URL:		http://unixcode.org/libcapsinetwork/
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		libcapsinetwork-gcc43-includes.patch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%patch0 -p1

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
rm -rf %{buildroot}
%makeinstall_std

%post -n %{libname}%{major} -p /sbin/ldconfig
%postun -n %{libname}%{major} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n %{libname}%{major}
%defattr(-,root,root)
%doc COPYING.LIB README
%{_libdir}/lib*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc ChangeLog NEWS
%{_includedir}/*
%{_libdir}/lib*.so
#%{_libdir}/lib*.a
%{_libdir}/lib*.la
