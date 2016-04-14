.. -*- coding: utf-8; mode: rst -*-

=======
video.h
=======

.. _`video_get_pts`:

VIDEO_GET_PTS
=============

.. c:function:: VIDEO_GET_PTS ()


.. _`video_get_pts.description`:

Description
-----------


Read the 33 bit presentation time stamp as defined
in ITU T-REC-H.222.0 / ISO/IEC 13818-1.

The PTS should belong to the currently played
frame if possible, but may also be a value close to it
like the PTS of the last decoded frame or the last PTS
extracted by the PES parser.

