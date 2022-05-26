#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD113FCAC3C4E599F (Nikolaus@rath.org)
#
Name     : sshfs
Version  : 3.7.3
Release  : 27
URL      : https://github.com/libfuse/sshfs/releases/download/sshfs-3.7.3/sshfs-3.7.3.tar.xz
Source0  : https://github.com/libfuse/sshfs/releases/download/sshfs-3.7.3/sshfs-3.7.3.tar.xz
Source1  : https://github.com/libfuse/sshfs/releases/download/sshfs-3.7.3/sshfs-3.7.3.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: sshfs-bin = %{version}-%{release}
Requires: sshfs-license = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : fuse-dev
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(fuse3)
BuildRequires : pkgconfig(gthread-2.0)

%description
This Project is Orphaned
========================
This project is no longer maintained or developed. Github issue tracking and pull requests have
therefore been disabled. The mailing list (see below) is still available for use.

%package bin
Summary: bin components for the sshfs package.
Group: Binaries
Requires: sshfs-license = %{version}-%{release}

%description bin
bin components for the sshfs package.


%package license
Summary: license components for the sshfs package.
Group: Default

%description license
license components for the sshfs package.


%prep
%setup -q -n sshfs-3.7.3
cd %{_builddir}/sshfs-3.7.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653583832
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/sshfs
cp %{_builddir}/sshfs-3.7.3/COPYING %{buildroot}/usr/share/package-licenses/sshfs/4cc77b90af91e615a64ae04893fdffa7939db84c
DESTDIR=%{buildroot} ninja -C builddir install
## install_append content
mv %{buildroot}/usr/sbin/* %{buildroot}/usr/bin/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mount.fuse.sshfs
/usr/bin/mount.sshfs
/usr/bin/sshfs

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sshfs/4cc77b90af91e615a64ae04893fdffa7939db84c
