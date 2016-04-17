.. -*- coding: utf-8; mode: rst -*-

=======
audio.h
=======


.. _`audio_get_pts`:

AUDIO_GET_PTS
=============

.. c:function:: AUDIO_GET_PTS ()



.. _`audio_get_pts.description`:

Description
-----------


Read the 33 bit presentation time stamp as defined
in ITU T-REC-H.222.0 / ISO/IEC 13818-1.

The PTS should belong to the currently played
frame if possible, but may also be a value close to it
like the PTS of the last decoded frame or the last PTS
extracted by the PES parser.

