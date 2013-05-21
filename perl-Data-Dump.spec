%define	upstream_name	 Data-Dump
%define upstream_version 1.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Pretty printing of data structures
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module provides a single function called dump() that takes a list
of values as its argument and produces a string as its result. The
string contains Perl code that, when evaled, produces a deep copy of
the original arguments. The string is formatted for easy reading.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorlib}/Data

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.190.0-4mdv2012.0
+ Revision: 765143
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.190.0-3
+ Revision: 763657
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.190.0-2
+ Revision: 667070
- mass rebuild

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.190.0-1mdv2011.0
+ Revision: 595094
- update to new version 1.19

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.170.0-2mdv2011.0
+ Revision: 564732
- rebuild for perl 5.12.1

* Wed Jul 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.170.0-1mdv2011.0
+ Revision: 553083
- update to 1.17

* Mon Jul 27 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.150.0-1mdv2010.1
+ Revision: 400640
- update to 1.15
- using %%perl_convert_version

* Tue Jan 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdv2009.1
+ Revision: 328905
- update to new version 1.14

* Sun Jan 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-1mdv2009.1
+ Revision: 324487
- update to new version 1.13

* Wed Oct 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2009.1
+ Revision: 296392
- update to new version 1.12

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2009.0
+ Revision: 277944
- update to new version 1.11

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.08-3mdv2009.0
+ Revision: 223590
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.08-2mdv2008.1
+ Revision: 180377
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.08-1mdv2008.0
+ Revision: 19844
- 1.08


* Thu May 25 2006 Scott Karns <scottk@mandriva.org> 1.06-2mdv2007.0
- Updated to comply with Mandriva perl packaging policies

* Tue Nov 16 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.06-1mdk
- 1.06

* Mon Apr 19 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.03-1mdk
- 1.03

* Wed Aug 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.04-7mdk
- rebuild for new perl
- drop Prefix tag
- don't use PREFIX
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.04-6mdk
- rebuild for new auto{prov,req}

