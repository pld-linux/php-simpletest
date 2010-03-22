%include	/usr/lib/rpm/macros.php
%define		php_min_version 5.2.0
%define		pkgname	simpletest
Summary:	Unit testing for PHP
Name:		php-%{pkgname}
Version:	1.0.1
Release:	0.6
License:	LGPL v2.1
Group:		Development/Languages/PHP
Source0:	http://downloads.sourceforge.net/project/%{pkgname}/%{pkgname}/%{pkgname}_%{version}/%{pkgname}_%{version}.tar.gz
# Source0-md5:	ab70ef7617b37a933499a630890461da
Patch0:		no-php4.patch
URL:		http://www.simpletest.org/
BuildRequires:	rpmbuild(macros) >= 1.461
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 4:%{php_min_version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define		_appdir			%{php_data_dir}/%{pkgname}
%define		_appdir			%{php_pear_dir}/%{pkgname}

# _phpdocdir / php_docdir / phpdoc_dir ?
%define		_phpdocdir		%{_docdir}/phpdoc

# internal deps
%define		_noautopear	pear(\.\./.*\.php) pear(invoker.php) pear(mock_objects.php) pear(socket.php) pear(test_case.php) pear(unit_tester.php) pear(simpletest/.*)

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
SimpleTest is an open source unit test framework for the PHP
programming language and was created by Marcus Baker. The test
structure is similar to JUnit/PHPUnit.

SimpleTest supports mock objects and can be used to automate the
regression testing of web applications with a scriptable HTTP Client
that can parse HTML pages and simulate things like clicking on links
and submitting forms.

%package phpdoc
Summary:	Online manual for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja online do %{pkgname}
Group:		Documentation
Requires:	php-dirs

%description phpdoc
Documentation for %{pkgname}.

%description phpdoc -l pl.UTF-8
Dokumentacja do %{pkgname}.

%prep
%setup -qc

# no php4
mv simpletest/reflection{_php5,}.php
rm simpletest/reflection_php4.php
mv simpletest/test/reflection{_php5,}_test.php
rm simpletest/test/reflection_php4_test.php
%patch0 -p0

mv %{pkgname}/docs .
mv simpletest/[HLRV]* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a %{pkgname}/* $RPM_BUILD_ROOT%{_appdir}

install -d $RPM_BUILD_ROOT%{_phpdocdir}/%{pkgname}
cp -a docs/* $RPM_BUILD_ROOT%{_phpdocdir}/%{pkgname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HELP_MY_TESTS_DONT_WORK_ANYMORE README
%{_appdir}

%files phpdoc
%defattr(644,root,root,755)
%dir %{_phpdocdir}/%{pkgname}
%lang(en) %{_phpdocdir}/%{pkgname}/en
%lang(fr) %{_phpdocdir}/%{pkgname}/fr
