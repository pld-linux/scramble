Summary:	Simple application to encrypt files
Summary(pl.UTF-8):	Prosta aplikacja do szyfrowania plików
Name:		scramble
Version:	4.5.0
Release:	1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/xffm/%{name}-%{version}.tar.gz
# Source0-md5:	e535de04979d5f614f6f6571bb5b09d8
URL:		http://xffm.sourceforge.net/scramble.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scramble is the tool used by the Xffm-filemanager to encrypt and
decrypt files.

%description -l pl.UTF-8
Scramble jest narzędziem używanym przez Xffm-filemanager do
szyfrowania i rozszyfrowywania plików.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/xffm

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/scramble
%{_mandir}/man1/scramble.1*
