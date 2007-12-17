%define	module	Data-Dump
%define name	perl-%{module}
%define	modprefix Data

%define version 1.08
%define release %mkrel 1

Summary: 	Pretty printing of data structures
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	Artistic/GPL
Group: 		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
BuildArch:	noarch
URL:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif

%description
This module provides a single function called dump() that takes a list
of values as its argument and produces a string as its result. The
string contains Perl code that, when evaled, produces a deep copy of
the original arguments. The string is formatted for easy reading.


%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/%{modprefix}

