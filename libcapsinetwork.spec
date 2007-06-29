%define	version	0.2.5
%define release	2mdk

%define major	0
%define libname %mklibname capsinetwork

Summary:	Network library for easy development of C++ server daemons
Name:		libcapsinetwork
Version:	%{version}
Release:	%{release}
License:	LGPL
Group:		System/Libraries
URL:		http://unixcode.org/libcapsinetwork/
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{SOURCE0}.sig
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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


%package	-n %{libname}%{major}-devel
Summary:	Development related files for %{name}
Group:		Development/C++
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{libname}-devel = %{version}-%{release}
Requires:	%{libname}%{major} = %{version}-%{release}

%description	-n %{libname}%{major}-devel
%{name} is a network library for C++ server daemons aimed at easy
development of server daemons.

You need to install this package if you want to develop or compile
any applications/libraries that needs %{name}.

%prep
%setup -q

%build
%configure2_5x
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

%files -n %{libname}%{major}-devel
%defattr(-,root,root)
%doc ChangeLog NEWS
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
