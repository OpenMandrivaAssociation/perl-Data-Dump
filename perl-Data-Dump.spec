%define	upstream_name	 Data-Dump
%define upstream_version 1.19

Name: 		perl-%{upstream_name}
Version: 	%perl_convert_version %{upstream_version}
Release: 	%mkrel 1

Summary: 	Pretty printing of data structures
License: 	Artistic/GPL
Group: 		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a single function called dump() that takes a list
of values as its argument and produces a string as its result. The
string contains Perl code that, when evaled, produces a deep copy of
the original arguments. The string is formatted for easy reading.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/Data

