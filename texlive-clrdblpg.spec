Name:		texlive-clrdblpg
Version:	47511
Release:	2
Summary:	Control pagestyle of pages left blank by \cleardoublepage
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/clrdblpg
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clrdblpg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clrdblpg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clrdblpg.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This tiny package allows easy manipulation of the headers and
footers on pages left blank by \cleardoublepage. By default,
LaTeX has no easy facilities for this. This package uses more
or less the algorithm listed in the fancyhdr package
documentation, with some better indentation and added
flexibility.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/clrdblpg
%{_texmfdistdir}/tex/latex/clrdblpg
%doc %{_texmfdistdir}/doc/latex/clrdblpg

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
