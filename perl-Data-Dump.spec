%define	modname	Data-Dump
%define modver 1.22

Summary:	Pretty printing of data structures
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Data/Data-Dump-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This module provides a single function called dump() that takes a list
of values as its argument and produces a string as its result. The
string contains Perl code that, when evaled, produces a deep copy of
the original arguments. The string is formatted for easy reading.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Data
%{_mandir}/man3/*


