#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : containerd
Version  : 1.6.8
Release  : 84
URL      : https://github.com/containerd/containerd/archive/refs/tags/v1.6.8.tar.gz
Source0  : https://github.com/containerd/containerd/archive/refs/tags/v1.6.8.tar.gz
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
%setup -q -n containerd-1.6.8
cd %{_builddir}/containerd-1.6.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661294580
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
## make_prepend content
export GOPATH=$HOME/go GO111MODULE="auto"
mkdir -p $HOME/go/src/github.com/containerd/
ln -s /builddir/build/BUILD/%{name}-%{version} $HOME/go/src/github.com/containerd/containerd
pushd $HOME/go/src/github.com/containerd/containerd
## make_prepend end
make  %{?_smp_mflags}  V=1 REVISION="" VERSION=%{version} EXTRA_TAGS="netgo osusergo"


%install
export SOURCE_DATE_EPOCH=1661294580
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/containerd
cp %{_builddir}/containerd-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/containerd-%{version}/vendor/github.com/AdaLogics/go-fuzz-headers/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/package-licenses/containerd/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
cp %{_builddir}/containerd-%{version}/vendor/github.com/Microsoft/hcsshim/LICENSE %{buildroot}/usr/share/package-licenses/containerd/56b820712432e458f05f883566ca8cd85dcdaad5
cp %{_builddir}/containerd-%{version}/vendor/github.com/Microsoft/hcsshim/pkg/go-runhcs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/beorn7/perks/LICENSE %{buildroot}/usr/share/package-licenses/containerd/b2e4520feb0f9b51ad373256b94c3faf4c1e6871
cp %{_builddir}/containerd-%{version}/vendor/github.com/blang/semver/LICENSE %{buildroot}/usr/share/package-licenses/containerd/16e22f58039363cff486afeac52bde18cd4ab5b3
cp %{_builddir}/containerd-%{version}/vendor/github.com/cenkalti/backoff/v4/LICENSE %{buildroot}/usr/share/package-licenses/containerd/101c182fa18fd56a09164278f17e4282264c5e9e
cp %{_builddir}/containerd-%{version}/vendor/github.com/cespare/xxhash/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/containerd/7be82c1a81e7197640a88df91dc82d64b77c7acd
cp %{_builddir}/containerd-%{version}/vendor/github.com/cilium/ebpf/LICENSE %{buildroot}/usr/share/package-licenses/containerd/27a6200050717015f18fdbd39387845787ce81a9
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/aufs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/btrfs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/cgroups/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/console/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/continuity/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/fifo/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/go-cni/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/go-runc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/imgcrypt/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/nri/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/ttrpc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/typeurl/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d3b7a70b03b43d4e7205d178100581923a0baad2
cp %{_builddir}/containerd-%{version}/vendor/github.com/containerd/zfs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/github.com/containernetworking/cni/LICENSE %{buildroot}/usr/share/package-licenses/containerd/669a1e53b9dd9df3474300d3d959bb85bad75945
cp %{_builddir}/containerd-%{version}/vendor/github.com/containernetworking/plugins/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-%{version}/vendor/github.com/containers/ocicrypt/LICENSE %{buildroot}/usr/share/package-licenses/containerd/3037fadf4c833d13c87fcd0b2f932de187edf676
cp %{_builddir}/containerd-%{version}/vendor/github.com/coreos/go-systemd/v22/LICENSE %{buildroot}/usr/share/package-licenses/containerd/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/containerd-%{version}/vendor/github.com/cpuguy83/go-md2man/v2/LICENSE.md %{buildroot}/usr/share/package-licenses/containerd/b7a606730713ac061594edab33cf941704b4a95c
cp %{_builddir}/containerd-%{version}/vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d2f340a01dd48b589a70f627cf7058c585a315e4
cp %{_builddir}/containerd-%{version}/vendor/github.com/docker/go-events/LICENSE %{buildroot}/usr/share/package-licenses/containerd/8e5643a553edd1143413a2ff85104539b7dbecca
cp %{_builddir}/containerd-%{version}/vendor/github.com/docker/go-metrics/LICENSE %{buildroot}/usr/share/package-licenses/containerd/376caa2cd54c4196280157d071524614350e7ce8
cp %{_builddir}/containerd-%{version}/vendor/github.com/docker/go-metrics/LICENSE.docs %{buildroot}/usr/share/package-licenses/containerd/979fd7d5c67073b265d96f584aac3de1c419b8e2
cp %{_builddir}/containerd-%{version}/vendor/github.com/docker/go-units/LICENSE %{buildroot}/usr/share/package-licenses/containerd/3110e55750143a84918d7423febc9c83a55bc28c
cp %{_builddir}/containerd-%{version}/vendor/github.com/emicklei/go-restful/LICENSE %{buildroot}/usr/share/package-licenses/containerd/a8993f4a51771a0333dbbc5b1c4395a2ccaa4d9f
cp %{_builddir}/containerd-%{version}/vendor/github.com/fsnotify/fsnotify/LICENSE %{buildroot}/usr/share/package-licenses/containerd/66a9502ecba0bae239ca6ba2c3e8a2fe5558a893
cp %{_builddir}/containerd-%{version}/vendor/github.com/go-logr/logr/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-%{version}/vendor/github.com/go-logr/stdr/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/godbus/dbus/v5/LICENSE %{buildroot}/usr/share/package-licenses/containerd/994658c265db5dbf456fa6163905cc9c0b3bda46
cp %{_builddir}/containerd-%{version}/vendor/github.com/gogo/googleapis/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7f8c8c31bf3ed5b6616225c00b5a960c2bbbae2f
cp %{_builddir}/containerd-%{version}/vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/containerd/06b27345acae9303e13dde9974d2b2e318b05989
cp %{_builddir}/containerd-%{version}/vendor/github.com/golang/groupcache/LICENSE %{buildroot}/usr/share/package-licenses/containerd/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/containerd-%{version}/vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/containerd/aa9b240f558caed367795f667629ccbca28f20b2
cp %{_builddir}/containerd-%{version}/vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7080652cc78cd9855d39e324529a3b5f3745dcd6
cp %{_builddir}/containerd-%{version}/vendor/github.com/google/gofuzz/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/github.com/google/uuid/LICENSE %{buildroot}/usr/share/package-licenses/containerd/08021ae73f58f423dd6e7b525e81cf2520f7619e
cp %{_builddir}/containerd-%{version}/vendor/github.com/grpc-ecosystem/go-grpc-middleware/LICENSE %{buildroot}/usr/share/package-licenses/containerd/482a69af7e9431b91119f958a5ee57f4c149808b
cp %{_builddir}/containerd-%{version}/vendor/github.com/grpc-ecosystem/go-grpc-prometheus/LICENSE %{buildroot}/usr/share/package-licenses/containerd/482a69af7e9431b91119f958a5ee57f4c149808b
cp %{_builddir}/containerd-%{version}/vendor/github.com/grpc-ecosystem/grpc-gateway/LICENSE.txt %{buildroot}/usr/share/package-licenses/containerd/c2add16c875ec7abad9c453d0a0c325dc814e8f2
cp %{_builddir}/containerd-%{version}/vendor/github.com/hashicorp/errwrap/LICENSE %{buildroot}/usr/share/package-licenses/containerd/523489384296f403da31edf8edf6f9023d328517
cp %{_builddir}/containerd-%{version}/vendor/github.com/hashicorp/go-multierror/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2ebe302ef4d8d257ac6f0a916285b51937a25641
cp %{_builddir}/containerd-%{version}/vendor/github.com/imdario/mergo/LICENSE %{buildroot}/usr/share/package-licenses/containerd/eecfc0c7e0930c6ba1ed0ff2d46a0a6fa0d16d6c
cp %{_builddir}/containerd-%{version}/vendor/github.com/intel/goresctrl/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/json-iterator/go/LICENSE %{buildroot}/usr/share/package-licenses/containerd/810612ee8c1872b7ee4dba34c090ebd8f7491aa1
cp %{_builddir}/containerd-%{version}/vendor/github.com/klauspost/compress/LICENSE %{buildroot}/usr/share/package-licenses/containerd/555ab8c87b6d441eb65c8afa9a11b7d8eb9e7640
cp %{_builddir}/containerd-%{version}/vendor/github.com/klauspost/compress/snappy/LICENSE %{buildroot}/usr/share/package-licenses/containerd/b7b97d84a5f0b778ab971d2afce44f47c8b6e80a
cp %{_builddir}/containerd-%{version}/vendor/github.com/klauspost/compress/zstd/internal/xxhash/LICENSE.txt %{buildroot}/usr/share/package-licenses/containerd/7be82c1a81e7197640a88df91dc82d64b77c7acd
cp %{_builddir}/containerd-%{version}/vendor/github.com/matttproud/golang_protobuf_extensions/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-%{version}/vendor/github.com/miekg/pkcs11/LICENSE %{buildroot}/usr/share/package-licenses/containerd/a347f428584b1ae13a669c007351ba7885597d59
cp %{_builddir}/containerd-%{version}/vendor/github.com/mistifyio/go-zfs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/b3c529b8fb7f1d56db7381bc7ef5f481ea2ac2a4
cp %{_builddir}/containerd-%{version}/vendor/github.com/moby/locker/LICENSE %{buildroot}/usr/share/package-licenses/containerd/600a7a38fdb246fd62c4e101868e6d0da9a3843c
cp %{_builddir}/containerd-%{version}/vendor/github.com/moby/spdystream/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/github.com/moby/sys/mountinfo/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/github.com/moby/sys/signal/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/github.com/moby/sys/symlink/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/github.com/moby/sys/symlink/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/containerd/de6aabbb551ff752e690d7a1136a5b5228f130cb
cp %{_builddir}/containerd-%{version}/vendor/github.com/moby/sys/symlink/LICENSE.BSD %{buildroot}/usr/share/package-licenses/containerd/818cd8d3934fc2af85e81c1f39c51ef7f661c139
cp %{_builddir}/containerd-%{version}/vendor/github.com/modern-go/concurrent/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/modern-go/reflect2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/opencontainers/go-digest/LICENSE %{buildroot}/usr/share/package-licenses/containerd/93ac97c9679b68518f1fd7de627ce2f77f44082d
cp %{_builddir}/containerd-%{version}/vendor/github.com/opencontainers/go-digest/LICENSE.docs %{buildroot}/usr/share/package-licenses/containerd/979fd7d5c67073b265d96f584aac3de1c419b8e2
cp %{_builddir}/containerd-%{version}/vendor/github.com/opencontainers/image-spec/LICENSE %{buildroot}/usr/share/package-licenses/containerd/298850a6cdb155f54cfa44641df70b36228ed031
cp %{_builddir}/containerd-%{version}/vendor/github.com/opencontainers/runc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
cp %{_builddir}/containerd-%{version}/vendor/github.com/opencontainers/runtime-spec/LICENSE %{buildroot}/usr/share/package-licenses/containerd/552b909d29bd260c886142a969b462c85f976dcd
cp %{_builddir}/containerd-%{version}/vendor/github.com/opencontainers/selinux/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-%{version}/vendor/github.com/pelletier/go-toml/LICENSE %{buildroot}/usr/share/package-licenses/containerd/0f506ab42c27323e32b4c8baa57cf7ddfc8d1b78
cp %{_builddir}/containerd-%{version}/vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/containerd/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
cp %{_builddir}/containerd-%{version}/vendor/github.com/pmezard/go-difflib/LICENSE %{buildroot}/usr/share/package-licenses/containerd/cd3e4d932cee20da681e6b3bee8139cb4f734034
cp %{_builddir}/containerd-%{version}/vendor/github.com/prometheus/client_golang/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/prometheus/client_golang/NOTICE %{buildroot}/usr/share/package-licenses/containerd/fd6460234f122a19f21affb6d6885269340b9176
cp %{_builddir}/containerd-%{version}/vendor/github.com/prometheus/client_model/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/prometheus/common/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/prometheus/procfs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/github.com/russross/blackfriday/v2/LICENSE.txt %{buildroot}/usr/share/package-licenses/containerd/da34754c05d40ff81f91de8c1b85ea6e5503e21d
cp %{_builddir}/containerd-%{version}/vendor/github.com/shurcooL/sanitized_anchor_name/LICENSE %{buildroot}/usr/share/package-licenses/containerd/c111106ab0af1873aa6350f797759fe1519c8be1
cp %{_builddir}/containerd-%{version}/vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/containerd/a1c7852c717fed2c9a0284ed112ea66013230da6
cp %{_builddir}/containerd-%{version}/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/containerd/b3c86ae465b21f7323059db335158b48187731c7
cp %{_builddir}/containerd-%{version}/vendor/github.com/stefanberger/go-pkcs11uri/LICENSE %{buildroot}/usr/share/package-licenses/containerd/c5c8a68f4b80929b3e66f054f37bb9e16078847f
cp %{_builddir}/containerd-%{version}/vendor/github.com/stretchr/testify/LICENSE %{buildroot}/usr/share/package-licenses/containerd/892204393ca075d09c8b1c1d880aba1ae0a2b805
cp %{_builddir}/containerd-%{version}/vendor/github.com/tchap/go-patricia/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7d3d6e2c0e14d20f475edae2f3936c574809efd5
cp %{_builddir}/containerd-%{version}/vendor/github.com/urfave/cli/LICENSE %{buildroot}/usr/share/package-licenses/containerd/62e85c543bad57a03eff756c0cfcb4bd26b77a4a
cp %{_builddir}/containerd-%{version}/vendor/github.com/vishvananda/netlink/LICENSE %{buildroot}/usr/share/package-licenses/containerd/f88291c879c4ee329bfa341b54eaedd29d3058cf
cp %{_builddir}/containerd-%{version}/vendor/github.com/vishvananda/netns/LICENSE %{buildroot}/usr/share/package-licenses/containerd/f88291c879c4ee329bfa341b54eaedd29d3058cf
cp %{_builddir}/containerd-%{version}/vendor/go.etcd.io/bbolt/LICENSE %{buildroot}/usr/share/package-licenses/containerd/66c5c002958b1f31f74410b353972d622d74e007
cp %{_builddir}/containerd-%{version}/vendor/go.mozilla.org/pkcs7/LICENSE %{buildroot}/usr/share/package-licenses/containerd/f9bbe972432aebdebf3469c89434273ba88ec9c7
cp %{_builddir}/containerd-%{version}/vendor/go.opencensus.io/LICENSE %{buildroot}/usr/share/package-licenses/containerd/1128f8f91104ba9ef98d37eea6523a888dcfa5de
cp %{_builddir}/containerd-%{version}/vendor/go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/go.opentelemetry.io/otel/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/go.opentelemetry.io/otel/exporters/otlp/internal/retry/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/go.opentelemetry.io/otel/exporters/otlp/otlptrace/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/go.opentelemetry.io/otel/sdk/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/go.opentelemetry.io/otel/trace/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/go.opentelemetry.io/proto/otlp/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/containerd-%{version}/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-%{version}/vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-%{version}/vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-%{version}/vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-%{version}/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-%{version}/vendor/golang.org/x/term/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-%{version}/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-%{version}/vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-%{version}/vendor/golang.org/x/xerrors/LICENSE %{buildroot}/usr/share/package-licenses/containerd/844fb1cc442e5f3d1800e47ae5d76d11a872b91c
cp %{_builddir}/containerd-%{version}/vendor/google.golang.org/appengine/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/google.golang.org/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/containerd/74850a25a5319bdddc0d998eb8926c18bada282b
cp %{_builddir}/containerd-%{version}/vendor/gopkg.in/inf.v0/LICENSE %{buildroot}/usr/share/package-licenses/containerd/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b
cp %{_builddir}/containerd-%{version}/vendor/gopkg.in/square/go-jose.v2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/gopkg.in/square/go-jose.v2/json/LICENSE %{buildroot}/usr/share/package-licenses/containerd/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
cp %{_builddir}/containerd-%{version}/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-%{version}/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/containerd/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/containerd-%{version}/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/containerd/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
cp %{_builddir}/containerd-%{version}/vendor/gopkg.in/yaml.v3/LICENSE %{buildroot}/usr/share/package-licenses/containerd/b74b3b31bc15ad5e94fc1947d682aa3d84132fce
cp %{_builddir}/containerd-%{version}/vendor/gopkg.in/yaml.v3/NOTICE %{buildroot}/usr/share/package-licenses/containerd/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
cp %{_builddir}/containerd-%{version}/vendor/gotest.tools/v3/LICENSE %{buildroot}/usr/share/package-licenses/containerd/c3001aa5b380f41731de929c562043693d7eb1ca
cp %{_builddir}/containerd-%{version}/vendor/gotest.tools/v3/internal/difflib/LICENSE %{buildroot}/usr/share/package-licenses/containerd/cd3e4d932cee20da681e6b3bee8139cb4f734034
cp %{_builddir}/containerd-%{version}/vendor/k8s.io/api/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/k8s.io/apimachinery/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/k8s.io/apimachinery/third_party/forked/golang/LICENSE %{buildroot}/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/containerd-%{version}/vendor/k8s.io/apiserver/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/k8s.io/client-go/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/k8s.io/component-base/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/k8s.io/cri-api/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-%{version}/vendor/k8s.io/klog/v2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/containerd-%{version}/vendor/k8s.io/utils/LICENSE %{buildroot}/usr/share/package-licenses/containerd/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/containerd-%{version}/vendor/sigs.k8s.io/structured-merge-diff/v4/LICENSE %{buildroot}/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/containerd-%{version}/vendor/sigs.k8s.io/yaml/LICENSE %{buildroot}/usr/share/package-licenses/containerd/271aeaf56ee621c5accfc2a9db0b10717e038eaf
%make_install PREFIX=/usr
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
/usr/share/package-licenses/containerd/0f506ab42c27323e32b4c8baa57cf7ddfc8d1b78
/usr/share/package-licenses/containerd/101c182fa18fd56a09164278f17e4282264c5e9e
/usr/share/package-licenses/containerd/1128f8f91104ba9ef98d37eea6523a888dcfa5de
/usr/share/package-licenses/containerd/11a8fec351554e8f6c3f4dac5a1f4049dd467ba8
/usr/share/package-licenses/containerd/16e22f58039363cff486afeac52bde18cd4ab5b3
/usr/share/package-licenses/containerd/172ca3bbafe312a1cf09cfff26953db2f425c28e
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
/usr/share/package-licenses/containerd/552b909d29bd260c886142a969b462c85f976dcd
/usr/share/package-licenses/containerd/555ab8c87b6d441eb65c8afa9a11b7d8eb9e7640
/usr/share/package-licenses/containerd/56b820712432e458f05f883566ca8cd85dcdaad5
/usr/share/package-licenses/containerd/580c0a1f1386fe13bce395d23bdaf3b14ae2e20b
/usr/share/package-licenses/containerd/600a7a38fdb246fd62c4e101868e6d0da9a3843c
/usr/share/package-licenses/containerd/62e85c543bad57a03eff756c0cfcb4bd26b77a4a
/usr/share/package-licenses/containerd/669a1e53b9dd9df3474300d3d959bb85bad75945
/usr/share/package-licenses/containerd/66a9502ecba0bae239ca6ba2c3e8a2fe5558a893
/usr/share/package-licenses/containerd/66c5c002958b1f31f74410b353972d622d74e007
/usr/share/package-licenses/containerd/7080652cc78cd9855d39e324529a3b5f3745dcd6
/usr/share/package-licenses/containerd/74850a25a5319bdddc0d998eb8926c18bada282b
/usr/share/package-licenses/containerd/7be82c1a81e7197640a88df91dc82d64b77c7acd
/usr/share/package-licenses/containerd/7d3d6e2c0e14d20f475edae2f3936c574809efd5
/usr/share/package-licenses/containerd/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/containerd/7f7a12bcfc16fab2522aa1a562fd3d2aee429d3b
/usr/share/package-licenses/containerd/7f8c8c31bf3ed5b6616225c00b5a960c2bbbae2f
/usr/share/package-licenses/containerd/810612ee8c1872b7ee4dba34c090ebd8f7491aa1
/usr/share/package-licenses/containerd/818cd8d3934fc2af85e81c1f39c51ef7f661c139
/usr/share/package-licenses/containerd/844fb1cc442e5f3d1800e47ae5d76d11a872b91c
/usr/share/package-licenses/containerd/892204393ca075d09c8b1c1d880aba1ae0a2b805
/usr/share/package-licenses/containerd/8e5643a553edd1143413a2ff85104539b7dbecca
/usr/share/package-licenses/containerd/8ff574408142cd6bbb2a1b83302de24cb7b35e8b
/usr/share/package-licenses/containerd/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/containerd/93ac97c9679b68518f1fd7de627ce2f77f44082d
/usr/share/package-licenses/containerd/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/containerd/979fd7d5c67073b265d96f584aac3de1c419b8e2
/usr/share/package-licenses/containerd/994658c265db5dbf456fa6163905cc9c0b3bda46
/usr/share/package-licenses/containerd/9c1bedc0d42f24c24a1bd266f3ce101a4b0579fc
/usr/share/package-licenses/containerd/a1c7852c717fed2c9a0284ed112ea66013230da6
/usr/share/package-licenses/containerd/a347f428584b1ae13a669c007351ba7885597d59
/usr/share/package-licenses/containerd/a8993f4a51771a0333dbbc5b1c4395a2ccaa4d9f
/usr/share/package-licenses/containerd/aa9b240f558caed367795f667629ccbca28f20b2
/usr/share/package-licenses/containerd/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/containerd/b2e4520feb0f9b51ad373256b94c3faf4c1e6871
/usr/share/package-licenses/containerd/b3c529b8fb7f1d56db7381bc7ef5f481ea2ac2a4
/usr/share/package-licenses/containerd/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/containerd/b74b3b31bc15ad5e94fc1947d682aa3d84132fce
/usr/share/package-licenses/containerd/b7a606730713ac061594edab33cf941704b4a95c
/usr/share/package-licenses/containerd/b7b97d84a5f0b778ab971d2afce44f47c8b6e80a
/usr/share/package-licenses/containerd/c111106ab0af1873aa6350f797759fe1519c8be1
/usr/share/package-licenses/containerd/c2add16c875ec7abad9c453d0a0c325dc814e8f2
/usr/share/package-licenses/containerd/c3001aa5b380f41731de929c562043693d7eb1ca
/usr/share/package-licenses/containerd/c5c8a68f4b80929b3e66f054f37bb9e16078847f
/usr/share/package-licenses/containerd/cd3e4d932cee20da681e6b3bee8139cb4f734034
/usr/share/package-licenses/containerd/d2f340a01dd48b589a70f627cf7058c585a315e4
/usr/share/package-licenses/containerd/d3b7a70b03b43d4e7205d178100581923a0baad2
/usr/share/package-licenses/containerd/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/containerd/da34754c05d40ff81f91de8c1b85ea6e5503e21d
/usr/share/package-licenses/containerd/de6aabbb551ff752e690d7a1136a5b5228f130cb
/usr/share/package-licenses/containerd/eecfc0c7e0930c6ba1ed0ff2d46a0a6fa0d16d6c
/usr/share/package-licenses/containerd/f88291c879c4ee329bfa341b54eaedd29d3058cf
/usr/share/package-licenses/containerd/f9bbe972432aebdebf3469c89434273ba88ec9c7
/usr/share/package-licenses/containerd/fd6460234f122a19f21affb6d6885269340b9176

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/containerd.service
