%define major 5
%define libname %mklibname KF5IMAP %{major}
%define devname %mklibname KF5IMAP -d
%define _disable_lto 1

Name: kimap
Version:	20.08.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for accessing IMAP servers
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Mime)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: sasl-devel
BuildRequires: boost-devel
Requires: %{libname} = %{EVRD}

%description
KDE library for accessing IMAP servers.

%package -n %{libname}
Summary: KDE library for accessing IMAP servers
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for accessing IMAP servers.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libkimap5

%files -f libkimap5.lang
%{_datadir}/qlogging-categories5/kimap.categories
%{_datadir}/qlogging-categories5/kimap.renamecategories

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
# kimaptest is built only as a static lib
%{_libdir}/*.a
