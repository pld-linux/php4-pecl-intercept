%define		_modname	intercept
%define		_status		alpha
%define		_sysconfdir	/etc/php4
%define		extensionsdir	%{_libdir}/php4
Summary:	%{_modname} - intercept function/method calls
Summary(pl.UTF-8):	%{_modname} - przechwytywanie wywołań funkcji/metod
Name:		php4-pecl-%{_modname}
Version:	0.3.0
Release:	0.1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	442121f4043984cdde213918266a925c
URL:		http://pecl.php.net/package/intercept/
BuildRequires:	php4-devel >= 4.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php4-common >= 3:4.4.0-3
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows the user to have a user-space function called when the
specified function is called. Support for class/object methods will be
added later.

In PECL status of this extension is: %{_status}.

%description -l pl.UTF-8
Pozwala użytkownikowi na określenie funkcji w przestrzeni użytkownika
wywoływanej, gdy określona funkcja jest wywołana. Wsparcie dla metod
klas/obiektów zostanie dodane w późniejszych wersjach.

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
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php4_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php4_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,EXPERIMENTAL}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
