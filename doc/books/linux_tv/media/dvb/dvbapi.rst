
.. _dvbapi:

+++++++++++++
LINUX DVB API
+++++++++++++

**Version 5.10**

.. toctree::
    :maxdepth: 1

    intro
    frontend
    demux
    ca
    net
    legacy_dvb_apis
    examples

.. _audio_h:

=====================
DVB Audio Header File
=====================


.. toctree::
    :maxdepth: 1

    ../../audio.h

.. _ca_h:

==================================
DVB Conditional Access Header File
==================================


.. toctree::
    :maxdepth: 1

    ../../ca.h

.. _dmx_h:

=====================
DVB Demux Header File
=====================


.. toctree::
    :maxdepth: 1

    ../../dmx.h

.. _frontend_h:

========================
DVB Frontend Header File
========================


.. toctree::
    :maxdepth: 1

    ../../frontend.h

.. _net_h:

=======================
DVB Network Header File
=======================


.. toctree::
    :maxdepth: 1

    ../../net.h

.. _video_h:

=====================
DVB Video Header File
=====================


.. toctree::
    :maxdepth: 1

    ../../video.h

======================
Revision and Copyright
======================


:author:    Metzler Ralph (*J. K.*)
:address:   rjkm@metzlerbros.de

:author:    Metzler Marcus (*O. C.*)
:address:   rjkm@metzlerbros.de

:author:    Chehab Mauro (*Carvalho*)
:address:   m.chehab@samsung.com
:contrib:   Ported document to Docbook XML.

**Copyright** 2002, 2003 : Convergence GmbH

**Copyright** 2009-2015 : Mauro Carvalho Chehab

:revision: 2.1.0 / 2015-05-29 (*mcc*)

DocBook improvements and cleanups, in order to document the system calls on a more standard way and provide more description about the current DVB API.


:revision: 2.0.4 / 2011-05-06 (*mcc*)

Add more information about DVB APIv5, better describing the frontend GET/SET props ioctl's.


:revision: 2.0.3 / 2010-07-03 (*mcc*)

Add some frontend capabilities flags, present on kernel, but missing at the specs.


:revision: 2.0.2 / 2009-10-25 (*mcc*)

documents FE_SET_FRONTEND_TUNE_MODE and FE_DISHETWORK_SEND_LEGACY_CMD ioctls.


:revision: 2.0.1 / 2009-09-16 (*mcc*)

Added ISDB-T test originally written by Patrick Boettcher


:revision: 2.0.0 / 2009-09-06 (*mcc*)

Conversion from LaTex to DocBook XML. The contents is the same as the original LaTex version.


:revision: 1.0.0 / 2003-07-24 (*rjkm*)

Initial revision on LaTEX.
