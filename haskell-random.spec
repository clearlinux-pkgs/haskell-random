Name     : haskell-random
Version  : 1.1
Release  : 1
URL      : http://hackage.haskell.org/package/random-1.1/random-1.1.tar.gz
Source0  : http://hackage.haskell.org/package/random-1.1/random-1.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause-Clear
BuildRequires: ghc-dev

%description
The Haskell Standard Library -- Random Number Generation

%prep
%setup -q -n random-1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555363563
runhaskell Setup configure --ghc --global \
--enable-static \
--enable-shared \
--enable-profiling \
--enable-executable-dynamic \
--enable-library-vanilla \
--enable-optimization=2 \
--prefix=/usr \
--dynlibdir=/usr/lib64/ghc-8.6.4/random-1.1 \
--libsubdir=/usr/lib64/ghc-8.6.4/random-1.1 \
--docdir=/usr/share/package-licenses/haskell-random
runhaskell Setup build
runhaskell Setup register --gen-pkg-config

%install
export SOURCE_DATE_EPOCH=1555363563
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/haskell-random
cp LICENSE %{buildroot}/usr/share/package-licenses/haskell-random/LICENSE
runhaskell Setup copy --destdir=%{buildroot}
mkdir -p %{buildroot}/usr/lib64/ghc-8.6.4/package.conf.d
cp random-1.1.conf %{buildroot}/usr/lib64/ghc-8.6.4/package.conf.d/random-1.1.conf

%files
%defattr(-,root,root,-)
/usr/lib64/ghc-8.6.4/package.conf.d/random-1.1.conf
/usr/lib64/ghc-8.6.4/random-1.1/System/Random.dyn_hi
/usr/lib64/ghc-8.6.4/random-1.1/System/Random.hi
/usr/lib64/ghc-8.6.4/random-1.1/System/Random.p_hi
/usr/lib64/ghc-8.6.4/random-1.1/libHSrandom-1.1-3ypV4EIycgb35PKjTYYr5q-ghc8.6.4.so
/usr/lib64/ghc-8.6.4/random-1.1/libHSrandom-1.1-3ypV4EIycgb35PKjTYYr5q.a
/usr/lib64/ghc-8.6.4/random-1.1/libHSrandom-1.1-3ypV4EIycgb35PKjTYYr5q_p.a
/usr/share/package-licenses/haskell-random/LICENSE
