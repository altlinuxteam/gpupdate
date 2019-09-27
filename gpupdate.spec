%define _unpackaged_files_terminate_build 1

Name:     gpupdate
Version:  0.1
Release:  alt2

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

BuildArch: noarch

%description
GPO applier

%prep
%setup

%install
install -Dm 0755 gpupdate %buildroot%_bindir/gpupdate
mkdir -p %buildroot/%python3_sitelibdir_noarch/gpoa
cp -av gpoa/* %buildroot/%python3_sitelibdir_noarch/gpoa

%files
%_bindir/%name
%python3_sitelibdir_noarch/gpoa

%changelog
* Tue Sep 24 2019 Igor Chudov <nir@altlinux.org> 0.1-alt2
- gpoa sources added

* Mon Sep 23 2019 Igor Chudov <nir@altlinux.org> 0.1-alt1
- Initial release

