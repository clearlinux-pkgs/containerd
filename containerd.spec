Name     : containerd
Version  : 1.0.2
Release  : 21
URL      : https://github.com/containerd/containerd/archive/v1.0.2.tar.gz
Source0  : https://github.com/containerd/containerd/archive/v1.0.2.tar.gz
Summary  : Daemon to control runC.
Group    : Development/Tools
License  : Apache-2.0
BuildRequires: btrfs-progs-dev
BuildRequires: go
BuildRequires: glibc-staticdev

%global goroot /usr/lib/golang
%global library_path github.com/containerd

%description
Containerd is a daemon to control runC, built for performance and density. Containerd leverages runC advanced features such as seccomp and user namespace support as well as checkpoint and restore for cloning and live migration of containers.

%package dev
Summary: dev components for the containerd package.
Group: Development

%description dev
dev components for the containerd package.

%prep
%setup -q -n containerd-%{version}

%build
export GOPATH=/go AUTO_GOPATH=1
mkdir -p /go/src/github.com/containerd/
ln -s /builddir/build/BUILD/%{name}-%{version} /go/src/github.com/containerd/containerd
pushd /go/src/github.com/containerd/containerd
make V=1 %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
install -d -p %{buildroot}%{_bindir}
install -p -m 755 bin/%{name} %{buildroot}%{_bindir}
install -p -m 755 bin/ctr %{buildroot}%{_bindir}/containerd-ctr
install -p -m 755 bin/containerd-shim %{buildroot}%{_bindir}

# Copy all *.go, *.s and *.proto files
install -d -p %{buildroot}%{goroot}/src/%{library_path}/
for ext in go s proto; do
	for file in $(find . -iname "*.$ext" | grep -v "^./Godeps") ; do
		install -d -p %{buildroot}%{goroot}/src/%{library_path}/$(dirname $file)
		cp -pav $file %{buildroot}%{goroot}/src/%{library_path}/$file
	done
done

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/containerd-ctr
%{_bindir}/containerd-shim

%files dev
%defattr(-,root,root,-)
%{goroot}/src/%{library_path}/*
