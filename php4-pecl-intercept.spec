%define		_modname	intercept
%define		_status		alpha

Summary:	%{_modname} - intercept function/method calls
Summary(pl):	%{_modname} - przechwytywanie wywo³añ funkcji/metod
Name:		php4-pecl-%{_modname}
Version:	0.2.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	fd5efb4a6d54047f9e935d975403c3ba
URL:		http://pecl.php.net/package/intercept/
BuildRequires:	libtool
BuildRequires:	php4-devel >= 4.0.0
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php4
%define		extensionsdir	%{_libdir}/php4

%description
Allows the user to have a user-space function called when the specified
function is called. Support for class/object methods will be added later.

In PECL status of this extension is: %{_status}.

%description -l pl
Pozwala u¿ytkownikowi na okre¶lenie funkcji w przestrzeni u¿ytkownika
wywo³ywanej, gdy okre¶lona funkcja jest wywo³ana. Wsparcie dla metod
klas/obiektów zostanie dodane w pó¼niejszych wersjach.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php4-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php4-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,EXPERIMENTAL}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
