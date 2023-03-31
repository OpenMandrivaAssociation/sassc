%global testspec_version 3.4.1

%bcond_with tests

Summary:	Wrapper around libsass to compile CSS stylesheet
Name:		sassc
Version:	3.6.2
Release:	2
License:	MIT
Group:		Development/Tools
Url:		http://github.com/sass/sassc
Source0:	https://github.com/sass/sassc/archive/%{name}-%{version}.tar.gz
# Test suite spec. According to this comment from an upstream dev, we should
# not use the release tags on the test spec:
# https://github.com/sass/libsass/issues/2258#issuecomment-268196004
# https://github.com/sass/sass-spec/archive/master.zip
# https://github.com/sass/sass-spec/archive/v%{testspec_version}.tar.gz
Source1:	sass-spec-%{testspec_version}.tar.gz
# libsass is built as a shared library.
#Patch0:		sassc-3.4.8-build.patch
BuildRequires:	pkgconfig(libsass) >= %{version}
%if %{with tests}
BuildRequires:	ruby
BuildRequires:	rubygem(minitest)
%endif

%description
SassC is a wrapper around libsass used to generate a useful command-line
application that can be installed and packaged for several operating systems.

%files
%doc LICENSE Readme.md
%{_bindir}/%{name}

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -a 1
mv sass-spec-%{testspec_version} sass-spec

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%if %{with tests}
%check
ruby sass-spec/sass-spec.rb -V 3.4 -c bin/%{name} --impl libsass sass-spec/spec
%endif
