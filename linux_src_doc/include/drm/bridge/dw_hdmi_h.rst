.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/bridge/dw_hdmi.h

.. _`supported-input-formats-and-encodings`:

Supported input formats and encodings
=====================================

Depending on the Hardware configuration of the Controller IP, it supports
a subset of the following input formats and encodings on its internal
48bit bus.

+----------------------+----------------------------------+------------------------------+
+ Format Name          + Format Code                      + Encodings                    +
+----------------------+----------------------------------+------------------------------+
+ RGB 4:4:4 8bit       + ``MEDIA_BUS_FMT_RGB888_1X24``    + ``V4L2_YCBCR_ENC_DEFAULT``   +
+----------------------+----------------------------------+------------------------------+
+ RGB 4:4:4 10bits     + ``MEDIA_BUS_FMT_RGB101010_1X30`` + ``V4L2_YCBCR_ENC_DEFAULT``   +
+----------------------+----------------------------------+------------------------------+
+ RGB 4:4:4 12bits     + ``MEDIA_BUS_FMT_RGB121212_1X36`` + ``V4L2_YCBCR_ENC_DEFAULT``   +
+----------------------+----------------------------------+------------------------------+
+ RGB 4:4:4 16bits     + ``MEDIA_BUS_FMT_RGB161616_1X48`` + ``V4L2_YCBCR_ENC_DEFAULT``   +
+----------------------+----------------------------------+------------------------------+
+ YCbCr 4:4:4 8bit     + ``MEDIA_BUS_FMT_YUV8_1X24``      + ``V4L2_YCBCR_ENC_601``       +
+                      +                                  + or ``V4L2_YCBCR_ENC_709``    +
+                      +                                  + or ``V4L2_YCBCR_ENC_XV601``  +
+                      +                                  + or ``V4L2_YCBCR_ENC_XV709``  +
+----------------------+----------------------------------+------------------------------+
+ YCbCr 4:4:4 10bits   + ``MEDIA_BUS_FMT_YUV10_1X30``     + ``V4L2_YCBCR_ENC_601``       +
+                      +                                  + or ``V4L2_YCBCR_ENC_709``    +
+                      +                                  + or ``V4L2_YCBCR_ENC_XV601``  +
+                      +                                  + or ``V4L2_YCBCR_ENC_XV709``  +
+----------------------+----------------------------------+------------------------------+
+ YCbCr 4:4:4 12bits   + ``MEDIA_BUS_FMT_YUV12_1X36``     + ``V4L2_YCBCR_ENC_601``       +
+                      +                                  + or ``V4L2_YCBCR_ENC_709``    +
+                      +                                  + or ``V4L2_YCBCR_ENC_XV601``  +
+                      +                                  + or ``V4L2_YCBCR_ENC_XV709``  +
+----------------------+----------------------------------+------------------------------+
+ YCbCr 4:4:4 16bits   + ``MEDIA_BUS_FMT_YUV16_1X48``     + ``V4L2_YCBCR_ENC_601``       +
+                      +                                  + or ``V4L2_YCBCR_ENC_709``    +
+                      +                                  + or ``V4L2_YCBCR_ENC_XV601``  +
+                      +                                  + or ``V4L2_YCBCR_ENC_XV709``  +
+----------------------+----------------------------------+------------------------------+
+ YCbCr 4:2:2 8bit     + ``MEDIA_BUS_FMT_UYVY8_1X16``     + ``V4L2_YCBCR_ENC_601``       +
+                      +                                  + or ``V4L2_YCBCR_ENC_709``    +
+----------------------+----------------------------------+------------------------------+
+ YCbCr 4:2:2 10bits   + ``MEDIA_BUS_FMT_UYVY10_1X20``    + ``V4L2_YCBCR_ENC_601``       +
+                      +                                  + or ``V4L2_YCBCR_ENC_709``    +
+----------------------+----------------------------------+------------------------------+
+ YCbCr 4:2:2 12bits   + ``MEDIA_BUS_FMT_UYVY12_1X24``    + ``V4L2_YCBCR_ENC_601``       +
+                      +                                  + or ``V4L2_YCBCR_ENC_709``    +
+----------------------+----------------------------------+------------------------------+
+ YCbCr 4:2:0 8bit     + ``MEDIA_BUS_FMT_UYYVYY8_0_5X24`` + ``V4L2_YCBCR_ENC_601``       +
+                      +                                  + or ``V4L2_YCBCR_ENC_709``    +
+----------------------+----------------------------------+------------------------------+
+ YCbCr 4:2:0 10bits   + ``MEDIA_BUS_FMT_UYYVYY10_0_5X30``+ ``V4L2_YCBCR_ENC_601``       +
+                      +                                  + or ``V4L2_YCBCR_ENC_709``    +
+----------------------+----------------------------------+------------------------------+
+ YCbCr 4:2:0 12bits   + ``MEDIA_BUS_FMT_UYYVYY12_0_5X36``+ ``V4L2_YCBCR_ENC_601``       +
+                      +                                  + or ``V4L2_YCBCR_ENC_709``    +
+----------------------+----------------------------------+------------------------------+
+ YCbCr 4:2:0 16bits   + ``MEDIA_BUS_FMT_UYYVYY16_0_5X48``+ ``V4L2_YCBCR_ENC_601``       +
+                      +                                  + or ``V4L2_YCBCR_ENC_709``    +
+----------------------+----------------------------------+------------------------------+

.. This file was automatic generated / don't edit.

