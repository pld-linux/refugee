Summary:	File encryption utility
Summary(pl.UTF-8):	Narzędzie do szyfrowania plików
Name:		refugee
Version:	0.99
Release:	3
License:	GPL
Group:		Applications/File
Source0:	http://www.synack.com/src/%{name}-%{version}.tar.gz
# Source0-md5:	ff2ec23b49bdc7f9d73abe1f8a8c9cb3
URL:		http://www.synack.com/soft.html
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Refugee is a file encryption and steganography utility. It implements
Blowfish and Rijndael in CBC mode and is portable between big- and
little-endian platforms. It supports key sizes from 32-448 bits and
gives the user many ways to make keys. It currently supports hiding
user data in PNG files.

%description -l pl.UTF-8
Refugee to narzędzie do szyfrowania plików i steganografii.
Implementuje algorytmy Blowfish i Rijndael w trybie CBC i jest
przenośny między platformami typu big- i little-endian. Może korzystać
z kluczy od 32 do 448 bitów, dając przy tym użytkownikowi wiele
róznych sposobów na stworzenie klucza. W chwili obecnej refugee
umożliwia ukrywanie danych użytkownika w plikach PNG.

%prep
%setup  -q

%build
./setup.sh
%{__make} CFLAGS="%{rpmcflags} -IRijndael \
	%{!?debug:-funroll-loops -fomit-frame-pointer} \
	-fno-strength-reduce -ffast-math" \
	PNG_LIB="-lpng"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	bindir=%{_bindir}

# names are too common...
cd $RPM_BUILD_ROOT%{_bindir}
for f in decrypt encrypt hide key ; do
	mv -f $f refugee-$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CHANGES CRYPTO README TODO
%attr(755,root,root) %{_bindir}/*
