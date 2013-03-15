%define		_class		PHP
%define		_subclass	CompatInfo
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.9.0
Release:	7
Summary:	Determine minimal requirements for a program
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/PHP_CompatInfo/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
PHP_CompatInfo will parse a file/folder/script/array to find out the
minimum version and extensions required for it to run. Features
advanced debug output which shows which functions require which
version.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_bindir}/scripts

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean


%files

%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_bindir}/pci
%{_bindir}/pciconf
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-6mdv2012.0
+ Revision: 742252
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-5
+ Revision: 679563
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-4mdv2011.0
+ Revision: 613756
- the mass rebuild of 2010.1 packages

* Sat Nov 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.9.0-3mdv2010.1
+ Revision: 467953
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.9.0-2mdv2010.0
+ Revision: 441551
- rebuild

* Sun Mar 22 2009 Funda Wang <fwang@mandriva.org> 1.9.0-1mdv2009.1
+ Revision: 360160
- New version 1.9.0

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-2mdv2009.1
+ Revision: 322652
- rebuild

* Mon Oct 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.1-1mdv2009.1
+ Revision: 293182
- update to new version 1.8.1

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-2mdv2009.0
+ Revision: 237050
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.4.3-1mdv2008.1
+ Revision: 140730
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.4.3-1mdv2008.0
+ Revision: 15920
- fix build
- 1.4.3


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdv2007.0
+ Revision: 82517
- Import php-pear-PHP_CompatInfo

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdk
- initial Mandriva package (PLD import)

