#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD113FCAC3C4E599F (Nikolaus@rath.org)
#
Name     : sshfs
Version  : 3.5.1
Release  : 19
URL      : https://github.com/libfuse/sshfs/releases/download/sshfs-3.5.1/sshfs-3.5.1.tar.xz
Source0  : https://github.com/libfuse/sshfs/releases/download/sshfs-3.5.1/sshfs-3.5.1.tar.xz
Source99 : https://github.com/libfuse/sshfs/releases/download/sshfs-3.5.1/sshfs-3.5.1.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: sshfs-bin = %{version}-%{release}
Requires: sshfs-license = %{version}-%{release}
Requires: sshfs-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : docutils
BuildRequires : fuse-dev
BuildRequires : pkgconfig(fuse)
BuildRequires : pkgconfig(gthread-2.0)

%description
SSHFS
=====
About
-----
SSHFS allows you to mount a remote filesystem using SFTP. Most SSH
servers support and enable this SFTP access by default, so SSHFS is
very simple to use - there's nothing to do on the server-side.

%package bin
Summary: bin components for the sshfs package.
Group: Binaries
Requires: sshfs-license = %{version}-%{release}
Requires: sshfs-man = %{version}-%{release}

%description bin
bin components for the sshfs package.


%package license
Summary: license components for the sshfs package.
Group: Default

%description license
license components for the sshfs package.


%package man
Summary: man components for the sshfs package.
Group: Default

%description man
man components for the sshfs package.


%prep
%setup -q -n sshfs-3.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545499170
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/sshfs
cp COPYING %{buildroot}/usr/share/package-licenses/sshfs/COPYING
DESTDIR=%{buildroot} ninja -C builddir install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sshfs
/usr/sbin/mount.fuse.sshfs
/usr/sbin/mount.sshfs

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sshfs/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sshfs.1
