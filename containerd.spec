#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : containerd
Version  : 1.3.0
Release  : 31
URL      : https://github.com/containerd/containerd/archive/v1.3.0.tar.gz
Source0  : https://github.com/containerd/containerd/archive/v1.3.0.tar.gz
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
%setup -q -n containerd-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570468539
export GCC_IGNORE_WERROR=1
export GOPROXY=file:///usr/share/goproxy
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
## make_prepend content
export GOPATH=/go GO111MODULES=off
mkdir -p /go/src/github.com/containerd/
ln -s /builddir/build/BUILD/%{name}-%{version} /go/src/github.com/containerd/containerd
pushd /go/src/github.com/containerd/containerd
## make_prepend end
make  %{?_smp_mflags}  V=1 REVISION="" VERSION=%{version}


%install
export SOURCE_DATE_EPOCH=1570468539
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/containerd
cp LICENSE %{buildroot}/usr/share/package-licenses/containerd/LICENSE
cp vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_BurntSushi_toml_COPYING
cp vendor/github.com/Microsoft/go-winio/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_Microsoft_go-winio_LICENSE
cp vendor/github.com/Microsoft/hcsshim/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_Microsoft_hcsshim_LICENSE
cp vendor/github.com/Microsoft/hcsshim/pkg/go-runhcs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_Microsoft_hcsshim_pkg_go-runhcs_LICENSE
cp vendor/github.com/beorn7/perks/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_beorn7_perks_LICENSE
cp vendor/github.com/containerd/aufs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containerd_aufs_LICENSE
cp vendor/github.com/containerd/btrfs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containerd_btrfs_LICENSE
cp vendor/github.com/containerd/cgroups/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containerd_cgroups_LICENSE
cp vendor/github.com/containerd/console/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containerd_console_LICENSE
cp vendor/github.com/containerd/continuity/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containerd_continuity_LICENSE
cp vendor/github.com/containerd/cri/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containerd_cri_LICENSE
cp vendor/github.com/containerd/fifo/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containerd_fifo_LICENSE
cp vendor/github.com/containerd/go-cni/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containerd_go-cni_LICENSE
cp vendor/github.com/containerd/go-runc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containerd_go-runc_LICENSE
cp vendor/github.com/containerd/ttrpc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containerd_ttrpc_LICENSE
cp vendor/github.com/containerd/typeurl/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containerd_typeurl_LICENSE
cp vendor/github.com/containerd/zfs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containerd_zfs_LICENSE
cp vendor/github.com/containernetworking/cni/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containernetworking_cni_LICENSE
cp vendor/github.com/containernetworking/plugins/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_containernetworking_plugins_LICENSE
cp vendor/github.com/coreos/go-systemd/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_coreos_go-systemd_LICENSE
cp vendor/github.com/cpuguy83/go-md2man/LICENSE.md %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_cpuguy83_go-md2man_LICENSE.md
cp vendor/github.com/davecgh/go-spew/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_davecgh_go-spew_LICENSE
cp vendor/github.com/docker/distribution/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_docker_distribution_LICENSE
cp vendor/github.com/docker/docker/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_docker_docker_LICENSE
cp vendor/github.com/docker/docker/NOTICE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_docker_docker_NOTICE
cp vendor/github.com/docker/docker/pkg/symlink/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_docker_docker_pkg_symlink_LICENSE.APACHE
cp vendor/github.com/docker/docker/pkg/symlink/LICENSE.BSD %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_docker_docker_pkg_symlink_LICENSE.BSD
cp vendor/github.com/docker/go-events/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_docker_go-events_LICENSE
cp vendor/github.com/docker/go-metrics/LICENSE.code %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_docker_go-metrics_LICENSE.code
cp vendor/github.com/docker/go-metrics/LICENSE.docs %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_docker_go-metrics_LICENSE.docs
cp vendor/github.com/docker/go-units/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_docker_go-units_LICENSE
cp vendor/github.com/docker/spdystream/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_docker_spdystream_LICENSE
cp vendor/github.com/docker/spdystream/LICENSE.docs %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_docker_spdystream_LICENSE.docs
cp vendor/github.com/emicklei/go-restful/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_emicklei_go-restful_LICENSE
cp vendor/github.com/godbus/dbus/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_godbus_dbus_LICENSE
cp vendor/github.com/gogo/googleapis/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_gogo_googleapis_LICENSE
cp vendor/github.com/gogo/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_gogo_protobuf_LICENSE
cp vendor/github.com/golang/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_golang_protobuf_LICENSE
cp vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_google_go-cmp_LICENSE
cp vendor/github.com/google/gofuzz/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_google_gofuzz_LICENSE
cp vendor/github.com/google/uuid/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_google_uuid_LICENSE
cp vendor/github.com/grpc-ecosystem/go-grpc-prometheus/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_grpc-ecosystem_go-grpc-prometheus_LICENSE
cp vendor/github.com/hashicorp/errwrap/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_hashicorp_errwrap_LICENSE
cp vendor/github.com/hashicorp/go-multierror/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_hashicorp_go-multierror_LICENSE
cp vendor/github.com/hashicorp/golang-lru/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_hashicorp_golang-lru_LICENSE
cp vendor/github.com/imdario/mergo/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_imdario_mergo_LICENSE
cp vendor/github.com/json-iterator/go/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_json-iterator_go_LICENSE
cp vendor/github.com/konsorten/go-windows-terminal-sequences/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_konsorten_go-windows-terminal-sequences_LICENSE
cp vendor/github.com/matttproud/golang_protobuf_extensions/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_matttproud_golang_protobuf_extensions_LICENSE
cp vendor/github.com/mistifyio/go-zfs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_mistifyio_go-zfs_LICENSE
cp vendor/github.com/modern-go/concurrent/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_modern-go_concurrent_LICENSE
cp vendor/github.com/modern-go/reflect2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_modern-go_reflect2_LICENSE
cp vendor/github.com/opencontainers/go-digest/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_opencontainers_go-digest_LICENSE
cp vendor/github.com/opencontainers/go-digest/LICENSE.docs %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_opencontainers_go-digest_LICENSE.docs
cp vendor/github.com/opencontainers/image-spec/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_opencontainers_image-spec_LICENSE
cp vendor/github.com/opencontainers/runc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_opencontainers_runc_LICENSE
cp vendor/github.com/opencontainers/runtime-spec/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_opencontainers_runtime-spec_LICENSE
cp vendor/github.com/opencontainers/selinux/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_opencontainers_selinux_LICENSE
cp vendor/github.com/pkg/errors/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_pkg_errors_LICENSE
cp vendor/github.com/prometheus/client_golang/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_prometheus_client_golang_LICENSE
cp vendor/github.com/prometheus/client_golang/NOTICE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_prometheus_client_golang_NOTICE
cp vendor/github.com/prometheus/client_model/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_prometheus_client_model_LICENSE
cp vendor/github.com/prometheus/common/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_prometheus_common_LICENSE
cp vendor/github.com/prometheus/procfs/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_prometheus_procfs_LICENSE
cp vendor/github.com/russross/blackfriday/LICENSE.txt %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_russross_blackfriday_LICENSE.txt
cp vendor/github.com/seccomp/libseccomp-golang/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_seccomp_libseccomp-golang_LICENSE
cp vendor/github.com/sirupsen/logrus/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_sirupsen_logrus_LICENSE
cp vendor/github.com/syndtr/gocapability/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_syndtr_gocapability_LICENSE
cp vendor/github.com/tchap/go-patricia/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_tchap_go-patricia_LICENSE
cp vendor/github.com/urfave/cli/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_github.com_urfave_cli_LICENSE
cp vendor/go.etcd.io/bbolt/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_go.etcd.io_bbolt_LICENSE
cp vendor/go.opencensus.io/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_go.opencensus.io_LICENSE
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/net/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_golang.org_x_net_LICENSE
cp vendor/golang.org/x/oauth2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_golang.org_x_oauth2_LICENSE
cp vendor/golang.org/x/sync/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_golang.org_x_sync_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_golang.org_x_sys_LICENSE
cp vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_golang.org_x_text_LICENSE
cp vendor/golang.org/x/time/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_golang.org_x_time_LICENSE
cp vendor/google.golang.org/genproto/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_google.golang.org_genproto_LICENSE
cp vendor/google.golang.org/grpc/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_google.golang.org_grpc_LICENSE
cp vendor/gopkg.in/inf.v0/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_gopkg.in_inf.v0_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_gopkg.in_yaml.v2_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/containerd/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
cp vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/containerd/vendor_gopkg.in_yaml.v2_NOTICE
cp vendor/gotest.tools/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_gotest.tools_LICENSE
cp vendor/gotest.tools/internal/difflib/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_gotest.tools_internal_difflib_LICENSE
cp vendor/k8s.io/api/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_k8s.io_api_LICENSE
cp vendor/k8s.io/apimachinery/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_k8s.io_apimachinery_LICENSE
cp vendor/k8s.io/apiserver/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_k8s.io_apiserver_LICENSE
cp vendor/k8s.io/client-go/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_k8s.io_client-go_LICENSE
cp vendor/k8s.io/cri-api/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_k8s.io_cri-api_LICENSE
cp vendor/k8s.io/klog/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_k8s.io_klog_LICENSE
cp vendor/k8s.io/kubernetes/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_k8s.io_kubernetes_LICENSE
cp vendor/k8s.io/utils/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_k8s.io_utils_LICENSE
cp vendor/sigs.k8s.io/yaml/LICENSE %{buildroot}/usr/share/package-licenses/containerd/vendor_sigs.k8s.io_yaml_LICENSE
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
/usr/share/package-licenses/containerd/LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_BurntSushi_toml_COPYING
/usr/share/package-licenses/containerd/vendor_github.com_Microsoft_go-winio_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_Microsoft_hcsshim_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_Microsoft_hcsshim_pkg_go-runhcs_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_beorn7_perks_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containerd_aufs_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containerd_btrfs_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containerd_cgroups_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containerd_console_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containerd_continuity_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containerd_cri_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containerd_fifo_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containerd_go-cni_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containerd_go-runc_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containerd_ttrpc_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containerd_typeurl_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containerd_zfs_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containernetworking_cni_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_containernetworking_plugins_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_coreos_go-systemd_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_cpuguy83_go-md2man_LICENSE.md
/usr/share/package-licenses/containerd/vendor_github.com_davecgh_go-spew_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_docker_distribution_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_docker_docker_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_docker_docker_NOTICE
/usr/share/package-licenses/containerd/vendor_github.com_docker_docker_pkg_symlink_LICENSE.APACHE
/usr/share/package-licenses/containerd/vendor_github.com_docker_docker_pkg_symlink_LICENSE.BSD
/usr/share/package-licenses/containerd/vendor_github.com_docker_go-events_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_docker_go-metrics_LICENSE.code
/usr/share/package-licenses/containerd/vendor_github.com_docker_go-metrics_LICENSE.docs
/usr/share/package-licenses/containerd/vendor_github.com_docker_go-units_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_docker_spdystream_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_docker_spdystream_LICENSE.docs
/usr/share/package-licenses/containerd/vendor_github.com_emicklei_go-restful_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_godbus_dbus_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_gogo_googleapis_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_gogo_protobuf_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_golang_protobuf_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_google_go-cmp_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_google_gofuzz_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_google_uuid_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_grpc-ecosystem_go-grpc-prometheus_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_hashicorp_errwrap_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_hashicorp_go-multierror_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_hashicorp_golang-lru_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_imdario_mergo_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_json-iterator_go_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_konsorten_go-windows-terminal-sequences_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_matttproud_golang_protobuf_extensions_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_mistifyio_go-zfs_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_modern-go_concurrent_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_modern-go_reflect2_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_opencontainers_go-digest_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_opencontainers_go-digest_LICENSE.docs
/usr/share/package-licenses/containerd/vendor_github.com_opencontainers_image-spec_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_opencontainers_runc_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_opencontainers_runtime-spec_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_opencontainers_selinux_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_pkg_errors_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_prometheus_client_golang_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_prometheus_client_golang_NOTICE
/usr/share/package-licenses/containerd/vendor_github.com_prometheus_client_model_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_prometheus_common_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_prometheus_procfs_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_russross_blackfriday_LICENSE.txt
/usr/share/package-licenses/containerd/vendor_github.com_seccomp_libseccomp-golang_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_sirupsen_logrus_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_syndtr_gocapability_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_tchap_go-patricia_LICENSE
/usr/share/package-licenses/containerd/vendor_github.com_urfave_cli_LICENSE
/usr/share/package-licenses/containerd/vendor_go.etcd.io_bbolt_LICENSE
/usr/share/package-licenses/containerd/vendor_go.opencensus.io_LICENSE
/usr/share/package-licenses/containerd/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/containerd/vendor_golang.org_x_net_LICENSE
/usr/share/package-licenses/containerd/vendor_golang.org_x_oauth2_LICENSE
/usr/share/package-licenses/containerd/vendor_golang.org_x_sync_LICENSE
/usr/share/package-licenses/containerd/vendor_golang.org_x_sys_LICENSE
/usr/share/package-licenses/containerd/vendor_golang.org_x_text_LICENSE
/usr/share/package-licenses/containerd/vendor_golang.org_x_time_LICENSE
/usr/share/package-licenses/containerd/vendor_google.golang.org_genproto_LICENSE
/usr/share/package-licenses/containerd/vendor_google.golang.org_grpc_LICENSE
/usr/share/package-licenses/containerd/vendor_gopkg.in_inf.v0_LICENSE
/usr/share/package-licenses/containerd/vendor_gopkg.in_yaml.v2_LICENSE
/usr/share/package-licenses/containerd/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
/usr/share/package-licenses/containerd/vendor_gopkg.in_yaml.v2_NOTICE
/usr/share/package-licenses/containerd/vendor_gotest.tools_LICENSE
/usr/share/package-licenses/containerd/vendor_gotest.tools_internal_difflib_LICENSE
/usr/share/package-licenses/containerd/vendor_k8s.io_api_LICENSE
/usr/share/package-licenses/containerd/vendor_k8s.io_apimachinery_LICENSE
/usr/share/package-licenses/containerd/vendor_k8s.io_apiserver_LICENSE
/usr/share/package-licenses/containerd/vendor_k8s.io_client-go_LICENSE
/usr/share/package-licenses/containerd/vendor_k8s.io_cri-api_LICENSE
/usr/share/package-licenses/containerd/vendor_k8s.io_klog_LICENSE
/usr/share/package-licenses/containerd/vendor_k8s.io_kubernetes_LICENSE
/usr/share/package-licenses/containerd/vendor_k8s.io_utils_LICENSE
/usr/share/package-licenses/containerd/vendor_sigs.k8s.io_yaml_LICENSE

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/containerd.service
