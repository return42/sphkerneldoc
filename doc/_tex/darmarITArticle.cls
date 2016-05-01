%
% ==============================================================================
% darmarITArticle.cls for Sphinx
% ==============================================================================

% Identifikation
% ========================================

\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{darmarITArticle}[2009/07/13 Document class (darmarIT Article)]

% Declaring options
% ========================================

% Pass remaining document options to the parent class.
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax


% Using classes and packages
% ========================================

\LoadClass{article}
\RequirePackage{fancyhdr}
\RequirePackage{eso-pic}

% Style parameters
% ========================================

\raggedbottom
\sloppy
\parindent = 0mm
\parskip = 2mm
\hbadness = 5000                % don't print trivial gripes


% Change the title page to look a bit better, and fit in with the fncychap
% ``Bjarne'' style a bit better.
%
\renewcommand{\maketitle}{
  \ifsphinxpdfoutput
    \begingroup
    % This \def is required to deal with multi-line authors; it
    % changes \\ to ', ' (comma-space), making it pass muster for
    % generating document info in the PDF file.
    \def\\{, }
    \pdfinfo{
      /Author (\@author)
      /Title (\@title)
    }
    \endgroup
  \fi
  \rule{\textwidth}{0.5pt}\par
  \vspace{10pt}
  \hfill{\normalfont\rmfamily\huge\py@HeaderFamily \@title}\par
  \rule{\textwidth}{0.5pt}\par
  {\py@HeaderFamily \@author} \hfill\@date\par
  \vspace{-40pt}
  %\vspace{15pt}
  %\py@authoraddress \par
  \thispagestyle{empty}
  \darmarITLogo
  \setcounter{footnote}{0}
  %\hfill
  %\@thanks
  %\darmarITpageNo
  %\let\thanks\relax\let\maketitle\relax
  %\gdef\@thanks{}\gdef\@author{}\gdef\@title{}
  %\par
  %{\em\large\py@HeaderFamily \py@release\releaseinfo}
}

% TOC
% ========================================

%% \let\py@OldTableofcontents=\tableofcontents
%% \renewcommand{\tableofcontents}{
%% \renewcommand*\contentsname{}
%%   \begin{small}
%%   \pagenumbering{arabic}
%%   \begingroup
%%     \parskip = 0mm
%%     \py@OldTableofcontents
%%   \endgroup
%%   \end{small}
%%   \rule{\textwidth}{0.5pt}
%%   \vspace{12pt}
%% }

% misc
% ========================================

\fancyfoot{} % clear all footer fields
\fancyhead{}

\fancypagestyle{normal}{
  \fancyhf{}
  %\fancyfoot[LE,RO]{{\darmarITpageNoRight}}
  \fancyfoot[LO]{{\darmarITpageNoLeft}}
  \fancyfoot[RE]{{\darmarITpageNoRight}}
  \fancyhead[LE,RO]{{\py@HeaderFamily \@title }}
  %\renewcommand{\headrulewidth}{0.4pt}
  %\renewcommand{\footrulewidth}{0.4pt}
}

% Update the plain style so we get the page number & footer line,
% but not a chapter or section title.  This is to keep the first
% page of a chapter and the blank page between chapters `clean.'
\fancypagestyle{plain}{
  \fancyhf{}
  \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
  %\renewcommand{\headrulewidth}{0pt}
  %\renewcommand{\footrulewidth}{0.4pt}
}


\thispagestyle{empty}
\setcounter{secnumdepth}{2}
\pagenumbering{arabic}
\pagestyle{normal}
