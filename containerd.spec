Name     : containerd
Version  : 0.1.0
Release  : 6
URL      : https://github.com/docker/containerd/archive/v0.2.0.tar.gz
Source0  : https://github.com/docker/containerd/archive/v0.2.0.tar.gz
Summary  : Daemon to control runC.
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : go
BuildRequires : glibc-staticdev

%global gopath /usr/lib/golang
%global library_path github.com/docker/

%description
Containerd is a daemon to control runC, built for performance and density. Containerd leverages runC advanced features such as seccomp and user namespace support as well as checkpoint and restore for cloning and live migration of containers.

%package dev
Summary: dev components for the containerd package.
Group: Development

%description dev
dev components for the containerd package.

%prep
%setup -q -n containerd-0.2.0

%build
mkdir -p src/github.com/docker/
ln -s $(pwd) src/github.com/docker/containerd
export GOPATH=$(pwd):%{gopath}
make V=1 %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -d -p %{buildroot}%{_bindir}
install -p -m 755 bin/%{name} %{buildroot}%{_bindir}
install -p -m 755 bin/ctr %{buildroot}%{_bindir}/containerd-ctr
install -p -m 755 bin/containerd-shim %{buildroot}%{_bindir}

# Copy all *.go, *.s and *.proto files
install -d -p %{buildroot}%{gopath}/src/%{library_path}/
for ext in go s proto; do
	for file in $(find . -iname "*.$ext" | grep -v "^./Godeps") ; do
		install -d -p %{buildroot}%{gopath}/src/%{library_path}/$(dirname $file)
		cp -pav $file %{buildroot}%{gopath}/src/%{library_path}/$file
	done
done

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_bindir}/containerd-ctr
%{_bindir}/containerd-shim

%files dev
%defattr(-,root,root,-)
%{gopath}/src/%{library_path}/*
