%global uuid logomenu@aryan_k

Name:          gnome-shell-extension-logo-menu
Version:       {{{ git_dir_version }}}
Release:       1%{?dist}
Summary:       Quick access menu for the GNOME panel

Group:         User Interface/Desktops
License:       GPLv2
URL:           https://github.com/ublue-os/Logomenu
Source0:       %{url}/archive/refs/heads/main.tar.gz
Source1:       %{url}/archive/refs/heads/gnome-44.tar.gz
BuildArch:     noarch

BuildRequires: make
BuildRequires: unzip
BuildRequires: gettext
BuildRequires: gnome-shell

Requires:    gnome-shell >= 3.12
%description
Quick access menu for the GNOME panel with options that help ease the workflow for newcomers and power users alike. 

%prep
%if 0%{?fedora} == 38
%setup -b 1 -n Logomenu-gnome-44
%else
%setup -n Logomenu-main
%endif

%install
make build
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
unzip logomenu@aryan_k.shell-extension.zip -d %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}

%files
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
{{{ git_dir_changelog }}}
