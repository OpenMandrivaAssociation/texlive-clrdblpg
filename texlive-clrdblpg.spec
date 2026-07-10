%global tl_name clrdblpg
%global tl_revision 47511

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Control pagestyle of pages left blank by \cleardoublepage
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/clrdblpg
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clrdblpg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clrdblpg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clrdblpg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This tiny package allows easy manipulation of the headers and footers on
pages left blank by \cleardoublepage. By default, LaTeX has no easy
facilities for this. This package uses more or less the algorithm listed
in the fancyhdr package documentation, with some better indentation and
added flexibility.

