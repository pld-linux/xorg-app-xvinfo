Summary:	xvinfo application to print X-Video extension adaptor information
Summary(pl.UTF-8):	Aplikacja xvinfo do wypisywania informacji o rozszerzeniu X-Video
Name:		xorg-app-xvinfo
Version:	1.1.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xvinfo-%{version}.tar.bz2
# Source0-md5:	8cc299b2cb636b5f7fe672610789d3d4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xvinfo prints out the capabilities of any video adaptors associated
with the display that are accessible through the X-Video extension.

%description -l pl.UTF-8
Program xvinfo wypisuje możliwości kart graficznych związanych z
wyświetlaczem, dostępnych poprzez rozszerzenie X-Video.

%prep
%setup -q -n xvinfo-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xvinfo
%{_mandir}/man1/xvinfo.1x*
