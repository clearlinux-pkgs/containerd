#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : containerd
Version  : 1.4.6
Release  : 66
URL      : https://github.com/containerd/containerd/archive/v1.4.6.tar.gz
Source0  : https://github.com/containerd/containerd/archive/v1.4.6.tar.gz
Summary  : An open and reliable container runtime
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 ISC MIT MPL-2.0 MPL-2.0-no-copyleft-exception
Requires: containerd-bin = %{version}-%{release}
Requires: containerd-license = %{version}-%{release}
Requires: containerd-services = %{version}-%{release}
BuildRequires : btrfs-progs-dev
BuildRequires : buildreq-golang
BuildRequires : libseccomp-dev

%description
An open and reliable container runtime

%package bin
Summary: bin components for the containerd package.
Group: Binaries
Requires: containerd-license = %{version}-%{release}
Requires: containerd-services = %{version}-%{release}

%description bin
bin components for the containerd package.


%package license
Summary: license components for the containerd package.
Group: Default

%description license
license components for the containerd package.


%package services
Summary: services components for the containerd package.
Group: Systemd services

%description services
services components for the containerd package.


%prep
%setup -q -n containerd-1.4.6
cd %{_builddir}/containerd-1.4.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1626130316
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
## make_prepend content
export GOPATH=$HOME/go GO111MODULE="auto"
mkdir -p $HOME/go/src/github.com/containerd/
ln -s /builddir/build/BUILD/%{name}-%{version} $HOME/go/src/github.com/containerd/containerd
pushd $HOME/go/src/github.com/containerd/containerd
## make_prepend end
make  %{?_smp_mflags}  V=1 REVISION="" VERSION=%{version} EXTRA_TAGS="netgo osusergo"


%install
export SOURCE_DATE_EPOCH=1626130316
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/containerd
cp %{_builddir}/containerd-1.4.6/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/containerd-1.4.6/vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/containerd/f9cab757896ef6b3570e62b2df7fb63ab1a34b80
cp %{_builddir}/containerd-1.4.6/vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/package-licenses/containerd/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
cp %{_builddir}/containerd-1.4.6/vendor/github.com/Microsoft/hcsshim/LICENSE %{buildroot}/usr/share/package-licenses/containerd/56b820712432e458f05f883566ca8cd85dcdaad5
cp %{_builddir}/containerd-1.4.6/vendor/github.com/Microsoft/hcsshim/pkg/go-runhcs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/beorn7/perks/LICENSE %{buildroot}/usr/share/package-licenses/containerd/b2e4520feb0f9b51ad373256b94c3faf4c1e6871
cp %{_builddir}/containerd-1.4.6/vendor/github.com/cespare/xxhash/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/containerd/7be82c1a81e7197640a88df91dc82d64b77c7acd
cp %{_builddir}/containerd-1.4.6/vendor/github.com/cilium/ebpf/LICENSE %{buildroot}/usr/share/package-licenses/containerd/27a6200050717015f18fdbd39387845787ce81a9
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/aufs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/btrfs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/cgroups/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/console/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/continuity/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/cri/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/fifo/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/go-cni/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/go-runc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/imgcrypt/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/ttrpc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/typeurl/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containerd/zfs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containernetworking/cni/LICENSE %{buildroot}/usr/share/package-licenses/containerd/669a1e53b9dd9df3474300d3d959bb85bad75945
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containernetworking/plugins/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-1.4.6/vendor/github.com/containers/ocicrypt/LICENSE %{buildroot}/usr/share/package-licenses/containerd/3037fadf4c833d13c87fcd0b2f932de187edf676
cp %{_builddir}/containerd-1.4.6/vendor/github.com/coreos/go-systemd/v22/LICENSE %{buildroot}/usr/share/package-licenses/containerd/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/containerd-1.4.6/vendor/github.com/cpuguy83/go-md2man/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/containerd/b7a606730713ac061594edab33cf941704b4a95c
cp %{_builddir}/containerd-1.4.6/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d2f340a01dd48b589a70f627cf7058c585a315e4
cp %{_builddir}/containerd-1.4.6/vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/package-licenses/containerd/20b06a68cf65738d43afa04acce0126f341c77f8
cp %{_builddir}/containerd-1.4.6/vendor/github.com/docker/docker/NOTICE %{buildroot}/usr/share/package-licenses/containerd/5476f2f91673ef040f1956907e7f45e72d5e11ee
cp %{_builddir}/containerd-1.4.6/vendor/github.com/docker/docker/pkg/symlink/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/containerd/de6aabbb551ff752e690d7a1136a5b5228f130cb
cp %{_builddir}/containerd-1.4.6/vendor/github.com/docker/docker/pkg/symlink/LICENSE.BSD %{buildroot}/usr/share/package-licenses/containerd/818cd8d3934fc2af85e81c1f39c51ef7f661c139
cp %{_builddir}/containerd-1.4.6/vendor/github.com/docker/go-events/LICENSE %{buildroot}/usr/share/package-licenses/containerd/8e5643a553edd1143413a2ff85104539b7dbecca
cp %{_builddir}/containerd-1.4.6/vendor/github.com/docker/go-metrics/LICENSE %{buildroot}/usr/share/package-licenses/containerd/376caa2cd54c4196280157d071524614350e7ce8
cp %{_builddir}/containerd-1.4.6/vendor/github.com/docker/go-metrics/LICENSE.docs %{buildroot}/usr/share/package-licenses/containerd/979fd7d5c67073b265d96f584aac3de1c419b8e2
cp %{_builddir}/containerd-1.4.6/vendor/github.com/docker/go-units/LICENSE %{buildroot}/usr/share/package-licenses/containerd/3110e55750143a84918d7423febc9c83a55bc28c
cp %{_builddir}/containerd-1.4.6/vendor/github.com/docker/spdystream/LICENSE %{buildroot}/usr/share/package-licenses/containerd/c6821d75aac4a65fae7d56a425e304beb3689c26
cp %{_builddir}/containerd-1.4.6/vendor/github.com/docker/spdystream/LICENSE.docs %{buildroot}/usr/share/package-licenses/containerd/979fd7d5c67073b265d96f584aac3de1c419b8e2
cp %{_builddir}/containerd-1.4.6/vendor/github.com/emicklei/go-restful/LICENSE %{buildroot}/usr/share/package-licenses/containerd/a8993f4a51771a0333dbbc5b1c4395a2ccaa4d9f
cp %{_builddir}/containerd-1.4.6/vendor/github.com/fsnotify/fsnotify/LICENSE %{buildroot}/usr/share/package-licenses/containerd/66a9502ecba0bae239ca6ba2c3e8a2fe5558a893
cp %{_builddir}/containerd-1.4.6/vendor/github.com/fullsailor/pkcs7/LICENSE %{buildroot}/usr/share/package-licenses/containerd/f9bbe972432aebdebf3469c89434273ba88ec9c7
cp %{_builddir}/containerd-1.4.6/vendor/github.com/go-logr/logr/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-1.4.6/vendor/github.com/godbus/dbus/v5/LICENSE %{buildroot}/usr/share/package-licenses/containerd/994658c265db5dbf456fa6163905cc9c0b3bda46
cp %{_builddir}/containerd-1.4.6/vendor/github.com/gogo/googleapis/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7f8c8c31bf3ed5b6616225c00b5a960c2bbbae2f
cp %{_builddir}/containerd-1.4.6/vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/containerd/06b27345acae9303e13dde9974d2b2e318b05989
cp %{_builddir}/containerd-1.4.6/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/containerd/aa9b240f558caed367795f667629ccbca28f20b2
cp %{_builddir}/containerd-1.4.6/vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7080652cc78cd9855d39e324529a3b5f3745dcd6
cp %{_builddir}/containerd-1.4.6/vendor/github.com/google/gofuzz/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-1.4.6/vendor/github.com/google/uuid/LICENSE %{buildroot}/usr/share/package-licenses/containerd/08021ae73f58f423dd6e7b525e81cf2520f7619e
cp %{_builddir}/containerd-1.4.6/vendor/github.com/grpc-ecosystem/go-grpc-prometheus/LICENSE %{buildroot}/usr/share/package-licenses/containerd/482a69af7e9431b91119f958a5ee57f4c149808b
cp %{_builddir}/containerd-1.4.6/vendor/github.com/hashicorp/errwrap/LICENSE %{buildroot}/usr/share/package-licenses/containerd/523489384296f403da31edf8edf6f9023d328517
cp %{_builddir}/containerd-1.4.6/vendor/github.com/hashicorp/go-multierror/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2ebe302ef4d8d257ac6f0a916285b51937a25641
cp %{_builddir}/containerd-1.4.6/vendor/github.com/hashicorp/golang-lru/LICENSE %{buildroot}/usr/share/package-licenses/containerd/ece3df1263c100f93c427face535a292723d38e7
cp %{_builddir}/containerd-1.4.6/vendor/github.com/imdario/mergo/LICENSE %{buildroot}/usr/share/package-licenses/containerd/eecfc0c7e0930c6ba1ed0ff2d46a0a6fa0d16d6c
cp %{_builddir}/containerd-1.4.6/vendor/github.com/json-iterator/go/LICENSE %{buildroot}/usr/share/package-licenses/containerd/810612ee8c1872b7ee4dba34c090ebd8f7491aa1
cp %{_builddir}/containerd-1.4.6/vendor/github.com/konsorten/go-windows-terminal-sequences/LICENSE %{buildroot}/usr/share/package-licenses/containerd/e2ee43b586677eaafd7dd7af25adff48adfa7cf3
cp %{_builddir}/containerd-1.4.6/vendor/github.com/matttproud/golang_protobuf_extensions/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-1.4.6/vendor/github.com/mistifyio/go-zfs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/b3c529b8fb7f1d56db7381bc7ef5f481ea2ac2a4
cp %{_builddir}/containerd-1.4.6/vendor/github.com/modern-go/concurrent/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/modern-go/reflect2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/opencontainers/go-digest/LICENSE %{buildroot}/usr/share/package-licenses/containerd/93ac97c9679b68518f1fd7de627ce2f77f44082d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/opencontainers/go-digest/LICENSE.docs %{buildroot}/usr/share/package-licenses/containerd/979fd7d5c67073b265d96f584aac3de1c419b8e2
cp %{_builddir}/containerd-1.4.6/vendor/github.com/opencontainers/image-spec/LICENSE %{buildroot}/usr/share/package-licenses/containerd/298850a6cdb155f54cfa44641df70b36228ed031
cp %{_builddir}/containerd-1.4.6/vendor/github.com/opencontainers/runc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
cp %{_builddir}/containerd-1.4.6/vendor/github.com/opencontainers/runtime-spec/LICENSE %{buildroot}/usr/share/package-licenses/containerd/552b909d29bd260c886142a969b462c85f976dcd
cp %{_builddir}/containerd-1.4.6/vendor/github.com/opencontainers/selinux/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-1.4.6/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/containerd/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
cp %{_builddir}/containerd-1.4.6/vendor/github.com/prometheus/client_golang/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/prometheus/client_golang/NOTICE %{buildroot}/usr/share/package-licenses/containerd/fd6460234f122a19f21affb6d6885269340b9176
cp %{_builddir}/containerd-1.4.6/vendor/github.com/prometheus/client_model/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/prometheus/common/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/prometheus/procfs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/russross/blackfriday/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/containerd/da34754c05d40ff81f91de8c1b85ea6e5503e21d
cp %{_builddir}/containerd-1.4.6/vendor/github.com/shurcooL/sanitized_anchor_name/LICENSE %{buildroot}/usr/share/package-licenses/containerd/c111106ab0af1873aa6350f797759fe1519c8be1
cp %{_builddir}/containerd-1.4.6/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/containerd/a1c7852c717fed2c9a0284ed112ea66013230da6
cp %{_builddir}/containerd-1.4.6/vendor/github.com/syndtr/gocapability/LICENSE %{buildroot}/usr/share/package-licenses/containerd/a44bfde22babd7c7e1ccac9ca31f85a09358769f
cp %{_builddir}/containerd-1.4.6/vendor/github.com/tchap/go-patricia/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7d3d6e2c0e14d20f475edae2f3936c574809efd5
cp %{_builddir}/containerd-1.4.6/vendor/github.com/urfave/cli/LICENSE %{buildroot}/usr/share/package-licenses/containerd/62e85c543bad57a03eff756c0cfcb4bd26b77a4a
cp %{_builddir}/containerd-1.4.6/vendor/github.com/willf/bitset/LICENSE %{buildroot}/usr/share/package-licenses/containerd/09a88870aebf0b3e52e5867531dcf3476ffb0b20
cp %{_builddir}/containerd-1.4.6/vendor/go.etcd.io/bbolt/LICENSE %{buildroot}/usr/share/package-licenses/containerd/66c5c002958b1f31f74410b353972d622d74e007
cp %{_builddir}/containerd-1.4.6/vendor/go.opencensus.io/LICENSE %{buildroot}/usr/share/package-licenses/containerd/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/containerd-1.4.6/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-1.4.6/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-1.4.6/vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-1.4.6/vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-1.4.6/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-1.4.6/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-1.4.6/vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-1.4.6/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-1.4.6/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-1.4.6/vendor/gopkg.in/inf.v0/LICENSE %{buildroot}/usr/share/package-licenses/containerd/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b
cp %{_builddir}/containerd-1.4.6/vendor/gopkg.in/square/go-jose.v2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-1.4.6/vendor/gopkg.in/square/go-jose.v2/json/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/containerd-1.4.6/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-1.4.6/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/containerd/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/containerd-1.4.6/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/containerd/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
cp %{_builddir}/containerd-1.4.6/vendor/gotest.tools/v3/LICENSE %{buildroot}/usr/share/package-licenses/containerd/c3001aa5b380f41731de929c562043693d7eb1ca
cp %{_builddir}/containerd-1.4.6/vendor/gotest.tools/v3/internal/difflib/LICENSE %{buildroot}/usr/share/package-licenses/containerd/cd3e4d932cee20da681e6b3bee8139cb4f734034
cp %{_builddir}/containerd-1.4.6/vendor/k8s.io/api/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-1.4.6/vendor/k8s.io/apimachinery/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-1.4.6/vendor/k8s.io/apiserver/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-1.4.6/vendor/k8s.io/client-go/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-1.4.6/vendor/k8s.io/cri-api/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-1.4.6/vendor/k8s.io/klog/v2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/containerd-1.4.6/vendor/k8s.io/utils/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-1.4.6/vendor/sigs.k8s.io/structured-merge-diff/v4/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-1.4.6/vendor/sigs.k8s.io/yaml/LICENSE %{buildroot}/usr/share/package-licenses/containerd/271aeaf56ee621c5accfc2a9db0b10717e038eaf
%make_install
## install_append content
sed -i -e 's:local/::' containerd.service
install -D -m 644 containerd.service %{buildroot}/usr/lib/systemd/system/containerd.service
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/containerd
/usr/bin/containerd-shim
/usr/bin/containerd-shim-runc-v1
/usr/bin/containerd-shim-runc-v2
/usr/bin/containerd-stress
/usr/bin/ctr

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/containerd/06b27345acae9303e13dde9974d2b2e318b05989
/usr/share/package-licenses/containerd/08021ae73f58f423dd6e7b525e81cf2520f7619e
/usr/share/package-licenses/containerd/09a88870aebf0b3e52e5867531dcf3476ffb0b20
/usr/share/package-licenses/containerd/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/containerd/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
/usr/share/package-licenses/containerd/172ca3bbafe312a1cf09cfff26953db2f425c28e
/usr/share/package-licenses/containerd/20b06a68cf65738d43afa04acce0126f341c77f8
/usr/share/package-licenses/containerd/271aeaf56ee621c5accfc2a9db0b10717e038eaf
/usr/share/package-licenses/containerd/27a6200050717015f18fdbd39387845787ce81a9
/usr/share/package-licenses/containerd/298850a6cdb155f54cfa44641df70b36228ed031
/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/containerd/2ebe302ef4d8d257ac6f0a916285b51937a25641
/usr/share/package-licenses/containerd/3037fadf4c833d13c87fcd0b2f932de187edf676
/usr/share/package-licenses/containerd/3110e55750143a84918d7423febc9c83a55bc28c
/usr/share/package-licenses/containerd/376caa2cd54c4196280157d071524614350e7ce8
/usr/share/package-licenses/containerd/482a69af7e9431b91119f958a5ee57f4c149808b
/usr/share/package-licenses/containerd/523489384296f403da31edf8edf6f9023d328517
/usr/share/package-licenses/containerd/5476f2f91673ef040f1956907e7f45e72d5e11ee
/usr/share/package-licenses/containerd/552b909d29bd260c886142a969b462c85f976dcd
/usr/share/package-licenses/containerd/56b820712432e458f05f883566ca8cd85dcdaad5
/usr/share/package-licenses/containerd/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b
/usr/share/package-licenses/containerd/62e85c543bad57a03eff756c0cfcb4bd26b77a4a
/usr/share/package-licenses/containerd/669a1e53b9dd9df3474300d3d959bb85bad75945
/usr/share/package-licenses/containerd/66a9502ecba0bae239ca6ba2c3e8a2fe5558a893
/usr/share/package-licenses/containerd/66c5c002958b1f31f74410b353972d622d74e007
/usr/share/package-licenses/containerd/7080652cc78cd9855d39e324529a3b5f3745dcd6
/usr/share/package-licenses/containerd/7be82c1a81e7197640a88df91dc82d64b77c7acd
/usr/share/package-licenses/containerd/7d3d6e2c0e14d20f475edae2f3936c574809efd5
/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/containerd/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
/usr/share/package-licenses/containerd/7f8c8c31bf3ed5b6616225c00b5a960c2bbbae2f
/usr/share/package-licenses/containerd/810612ee8c1872b7ee4dba34c090ebd8f7491aa1
/usr/share/package-licenses/containerd/818cd8d3934fc2af85e81c1f39c51ef7f661c139
/usr/share/package-licenses/containerd/8e5643a553edd1143413a2ff85104539b7dbecca
/usr/share/package-licenses/containerd/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/containerd/93ac97c9679b68518f1fd7de627ce2f77f44082d
/usr/share/package-licenses/containerd/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/containerd/979fd7d5c67073b265d96f584aac3de1c419b8e2
/usr/share/package-licenses/containerd/994658c265db5dbf456fa6163905cc9c0b3bda46
/usr/share/package-licenses/containerd/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/containerd/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/containerd/a44bfde22babd7c7e1ccac9ca31f85a09358769f
/usr/share/package-licenses/containerd/a8993f4a51771a0333dbbc5b1c4395a2ccaa4d9f
/usr/share/package-licenses/containerd/aa9b240f558caed367795f667629ccbca28f20b2
/usr/share/package-licenses/containerd/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/containerd/b2e4520feb0f9b51ad373256b94c3faf4c1e6871
/usr/share/package-licenses/containerd/b3c529b8fb7f1d56db7381bc7ef5f481ea2ac2a4
/usr/share/package-licenses/containerd/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/containerd/c111106ab0af1873aa6350f797759fe1519c8be1
/usr/share/package-licenses/containerd/c3001aa5b380f41731de929c562043693d7eb1ca
/usr/share/package-licenses/containerd/c6821d75aac4a65fae7d56a425e304beb3689c26
/usr/share/package-licenses/containerd/cd3e4d932cee20da681e6b3bee8139cb4f734034
/usr/share/package-licenses/containerd/d2f340a01dd48b589a70f627cf7058c585a315e4
/usr/share/package-licenses/containerd/d3b7a70b03b43d4e7205d178100581923a0baad2
/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/containerd/da34754c05d40ff81f91de8c1b85ea6e5503e21d
/usr/share/package-licenses/containerd/de6aabbb551ff752e690d7a1136a5b5228f130cb
/usr/share/package-licenses/containerd/e2ee43b586677eaafd7dd7af25adff48adfa7cf3
/usr/share/package-licenses/containerd/ece3df1263c100f93c427face535a292723d38e7
/usr/share/package-licenses/containerd/eecfc0c7e0930c6ba1ed0ff2d46a0a6fa0d16d6c
/usr/share/package-licenses/containerd/f9bbe972432aebdebf3469c89434273ba88ec9c7
/usr/share/package-licenses/containerd/f9cab757896ef6b3570e62b2df7fb63ab1a34b80
/usr/share/package-licenses/containerd/fd6460234f122a19f21affb6d6885269340b9176

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/containerd.service
