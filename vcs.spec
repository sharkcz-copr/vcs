%global longname video-contact-sheet

Name:           vcs
Summary:        Tool to create contact sheets (previews) from videos
Version:        1.13.4
Release:        3%{?dist}
License:        LGPLv2+
URL:            https://p.outlyer.net/vcs/
Source0:        https://github.com/outlyer-net/%{longname}/archive/%{version}/%{name}-%{version}.tar.gz
# update syntax for newer ImageMagick
Patch0:         vcs-1.13.4-imagemagick.patch
# egrep warns about its obsolescence in F-38
Patch1:         vcs-1.13.4-grep.patch
# updates for ImageMagick 7
Patch2:         vcs-1.13.4-imagemagick-7.patch
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
# satisfied by ffmpeg-free from Fedora or by ffmpeg from RPMFusion
Requires:       /usr/bin/ffmpeg
Requires:       ImageMagick
Requires:       coreutils
Requires:       gawk


%description
Video Contact Sheet *NIX (vcs for short) is a script that creates a contact
sheet (preview) from videos by taking still captures distributed over the
length of the video. The output image contains useful information on the video
such as codecs, file size, screen size, frame rate, and length.

%prep
%autosetup -p1 -n %{longname}-%{version}

# use pcansi terminal instead of pc3, which is not included in ncurses-base
sed -i 's/pc3/pcansi/' vcs


%build
cd dist/docs
make vcs.1 DOCBOOK_XSL=/usr/share/sgml/docbook/xsl-stylesheets


%install
cd dist
make DESTDIR=%{buildroot} prefix=%{_prefix} install


%files
%doc dist/CHANGELOG
%doc dist/examples/vcs.conf.example
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/profiles
%{_datadir}/%{name}/profiles/black.conf
%{_datadir}/%{name}/profiles/mosaic.conf
%{_datadir}/%{name}/profiles/white.conf
%{_datadir}/%{name}/profiles/compact.conf
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*


%changelog
* Mon Jun 24 2024 Dan Horák <dan[at]danny.cz> - 1.13.4-3
- updates for ImageMagick 7

* Wed Dec 27 2023 Dan Horák <dan[at]danny.cz> - 1.13.4-2
- updates for F-38+

* Mon Jun 20 2022 Dan Horák <dan[at]danny.cz> - 1.13.4-1
- initial Fedora version
