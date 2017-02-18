Name:		proxychains-ng
Version:	4.12
Release:	1%{?dist}
Summary:	Redirect connections through proxy servers
Group:		Applications/Internet

License:	GPLv2+
URL:		https://github.com/rofl0r/proxychains-ng
Source0:	%{name}-%{version}.tar.gz

Provides:	proxychains = %{version}
Obsoletes:	proxychains < %{version}

%description
ProxyChains NG is based on ProxyChains.

ProxyChains NG hooks network-related (TCP only) libc functions in dynamically
linked programs via a preloaded DSO (dynamic shared object) and redirects the
connections through one or more SOCKS4a/5 or HTTP proxies.

Since Proxy Chains NG relies on the dynamic linker, statically linked binaries
are not supported.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install install-config

%files
%license COPYING
%doc AUTHORS README TODO
%config(noreplace) %{_sysconfdir}/proxychains.conf
%{_bindir}/*
%{_libdir}/*

%changelog
* Sun Feb 19 2017 avl <avlubimov@gmail.com> 4.12-1
- new package built with tito

