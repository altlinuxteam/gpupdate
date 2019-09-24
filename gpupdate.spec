%define _unpackaged_files_terminate_build 1

Name:     gpupdate
Version:  0.1
Release:  alt1

Summary:  GPO applier
License:  GPLv2+
Group:    Other
Url:      http://altlinux.org

Packager: Igor Chudov <nir@altlinux.org>

Source:   %name-%version.tar

BuildRequires: rpm-build-python3
Requires: krb5-kinit
Requires: samba-common-tools
Requires: samba-client
Requires: samba-winbind
Requires: hreg
Requires: %name-templates

BuildArch: noarch

%description
GPO applier

%prep
%setup

%install
install -Dm 0755 gpupdate %buildroot%_bindir/gpupdate
mkdir -p %buildroot/%_libexecdir/gpoa
cp -av gpoa/* %buildroot/%_libexecdir/gpoa

%files
%_bindir/%name
%_libexecdir/gpoa

%changelog
* Mon Sep 23 2019 Igor Chudov <nir@altlinux.org> 0.1-alt1
- Initial release

