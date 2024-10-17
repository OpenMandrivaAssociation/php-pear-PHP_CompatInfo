%define		_class		PHP
%define		_subclass	CompatInfo
%define		upstream_name	%{_class}_%{_subclass}
%define __noautoreq /usr/bin/php

Name:		php-pear-%{upstream_name}
Version:	1.9.0
Release:	8
Summary:	Determine minimal requirements for a program

License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/PHP_CompatInfo/
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

%doc %{upstream_name}-%{version}/docs/*
%{_bindir}/pci
%{_bindir}/pciconf
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


