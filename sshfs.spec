#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sshfs
Version  : 2.9
Release  : 9
URL      : https://github.com/libfuse/sshfs/releases/download/sshfs-2.9/sshfs-2.9.tar.gz
Source0  : https://github.com/libfuse/sshfs/releases/download/sshfs-2.9/sshfs-2.9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: sshfs-bin
Requires: sshfs-doc
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(gthread-2.0)

%description
No detailed description available

%package bin
Summary: bin components for the sshfs package.
Group: Binaries

%description bin
bin components for the sshfs package.


%package doc
Summary: doc components for the sshfs package.
Group: Documentation

%description doc
doc components for the sshfs package.


%prep
%setup -q -n sshfs-2.9

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492481602
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1492481602
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sshfs

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
