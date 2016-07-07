.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/omap3isp.h

.. _`omap3isp_h3a_aewb_config`:

struct omap3isp_h3a_aewb_config
===============================

.. c:type:: struct omap3isp_h3a_aewb_config

    AE AWB configuration reset values

.. _`omap3isp_h3a_aewb_config.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_h3a_aewb_config {
        __u32 buf_size;
        __u16 config_counter;
        __u16 saturation_limit;
        __u16 win_height;
        __u16 win_width;
        __u16 ver_win_count;
        __u16 hor_win_count;
        __u16 ver_win_start;
        __u16 hor_win_start;
        __u16 blk_ver_win_start;
        __u16 blk_win_height;
        __u16 subsample_ver_inc;
        __u16 subsample_hor_inc;
        __u8 alaw_enable;
    }

.. _`omap3isp_h3a_aewb_config.members`:

Members
-------

buf_size
    *undescribed*

config_counter
    *undescribed*

saturation_limit
    *undescribed*

win_height
    Window Height. Range 2 - 256, even values only.

win_width
    Window Width. Range 6 - 256, even values only.

ver_win_count
    Vertical Window Count. Range 1 - 128.

hor_win_count
    Horizontal Window Count. Range 1 - 36.

ver_win_start
    Vertical Window Start. Range 0 - 4095.

hor_win_start
    Horizontal Window Start. Range 0 - 4095.

blk_ver_win_start
    Black Vertical Windows Start. Range 0 - 4095.

blk_win_height
    Black Window Height. Range 2 - 256, even values only.

subsample_ver_inc
    Subsample Vertical points increment Range 2 - 32, even
    values only.

subsample_hor_inc
    Subsample Horizontal points increment Range 2 - 32, even
    values only.

alaw_enable
    AEW ALAW EN flag.

.. _`omap3isp_h3a_aewb_config.saturation_limit`:

saturation_limit
----------------

Saturation limit.

.. _`omap3isp_stat_data`:

struct omap3isp_stat_data
=========================

.. c:type:: struct omap3isp_stat_data

    Statistic data sent to or received from user

.. _`omap3isp_stat_data.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_stat_data {
        struct timeval ts;
        void __user *buf;
        __u32 buf_size;
        __u16 frame_number;
        __u16 cur_frame;
        __u16 config_counter;
    }

.. _`omap3isp_stat_data.members`:

Members
-------

ts
    Timestamp of returned framestats.

buf
    Pointer to pass to user.

buf_size
    *undescribed*

frame_number
    Frame number of requested stats.

cur_frame
    Current frame number being processed.

config_counter
    Number of the configuration associated with the data.

.. _`omap3isp_ccdc_lsc_config`:

struct omap3isp_ccdc_lsc_config
===============================

.. c:type:: struct omap3isp_ccdc_lsc_config

    LSC configuration

.. _`omap3isp_ccdc_lsc_config.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_ccdc_lsc_config {
        __u16 offset;
        __u8 gain_mode_n;
        __u8 gain_mode_m;
        __u8 gain_format;
        __u16 fmtsph;
        __u16 fmtlnh;
        __u16 fmtslv;
        __u16 fmtlnv;
        __u8 initial_x;
        __u8 initial_y;
        __u32 size;
    }

.. _`omap3isp_ccdc_lsc_config.members`:

Members
-------

offset
    Table Offset of the gain table.

gain_mode_n
    Vertical dimension of a paxel in LSC configuration.

gain_mode_m
    Horizontal dimension of a paxel in LSC configuration.

gain_format
    Gain table format.

fmtsph
    Start pixel horizontal from start of the HS sync pulse.

fmtlnh
    Number of pixels in horizontal direction to use for the data
    reformatter.

fmtslv
    Start line from start of VS sync pulse for the data reformatter.

fmtlnv
    Number of lines in vertical direction for the data reformatter.

initial_x
    X position, in pixels, of the first active pixel in reference
    to the first active paxel. Must be an even number.

initial_y
    Y position, in pixels, of the first active pixel in reference
    to the first active paxel. Must be an even number.

size
    Size of LSC gain table. Filled when loaded from userspace.

.. _`omap3isp_ccdc_bclamp`:

struct omap3isp_ccdc_bclamp
===========================

.. c:type:: struct omap3isp_ccdc_bclamp

    Optical & Digital black clamp subtract

.. _`omap3isp_ccdc_bclamp.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_ccdc_bclamp {
        __u8 obgain;
        __u8 obstpixel;
        __u8 oblines;
        __u8 oblen;
        __u16 dcsubval;
    }

.. _`omap3isp_ccdc_bclamp.members`:

Members
-------

obgain
    Optical black average gain.

obstpixel
    Start Pixel w.r.t. HS pulse in Optical black sample.

oblines
    Optical Black Sample lines.

oblen
    Optical Black Sample Length.

dcsubval
    Digital Black Clamp subtract value.

.. _`omap3isp_ccdc_fpc`:

struct omap3isp_ccdc_fpc
========================

.. c:type:: struct omap3isp_ccdc_fpc

    Faulty Pixels Correction

.. _`omap3isp_ccdc_fpc.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_ccdc_fpc {
        __u16 fpnum;
        __u32 fpcaddr;
    }

.. _`omap3isp_ccdc_fpc.members`:

Members
-------

fpnum
    Number of faulty pixels to be corrected in the frame.

fpcaddr
    Memory address of the FPC Table

.. _`omap3isp_ccdc_blcomp`:

struct omap3isp_ccdc_blcomp
===========================

.. c:type:: struct omap3isp_ccdc_blcomp

    Black Level Compensation parameters

.. _`omap3isp_ccdc_blcomp.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_ccdc_blcomp {
        __u8 b_mg;
        __u8 gb_g;
        __u8 gr_cy;
        __u8 r_ye;
    }

.. _`omap3isp_ccdc_blcomp.members`:

Members
-------

b_mg
    B/Mg pixels. 2's complement. -128 to +127.

gb_g
    Gb/G pixels. 2's complement. -128 to +127.

gr_cy
    Gr/Cy pixels. 2's complement. -128 to +127.

r_ye
    R/Ye pixels. 2's complement. -128 to +127.

.. _`omap3isp_prev_hmed`:

struct omap3isp_prev_hmed
=========================

.. c:type:: struct omap3isp_prev_hmed

    Horizontal Median Filter

.. _`omap3isp_prev_hmed.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_hmed {
        __u8 odddist;
        __u8 evendist;
        __u8 thres;
    }

.. _`omap3isp_prev_hmed.members`:

Members
-------

odddist
    Distance between consecutive pixels of same color in the odd line.

evendist
    Distance between consecutive pixels of same color in the even
    line.

thres
    Horizontal median filter threshold.

.. _`omap3isp_prev_cfa`:

struct omap3isp_prev_cfa
========================

.. c:type:: struct omap3isp_prev_cfa

    CFA Interpolation

.. _`omap3isp_prev_cfa.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_cfa {
        enum omap3isp_cfa_fmt format;
        __u8 gradthrs_vert;
        __u8 gradthrs_horz;
        __u32 table[4][OMAP3ISP_PREV_CFA_BLK_SIZE];
    }

.. _`omap3isp_prev_cfa.members`:

Members
-------

format
    CFA Format Enum value supported by preview.

gradthrs_vert
    CFA Gradient Threshold - Vertical.

gradthrs_horz
    CFA Gradient Threshold - Horizontal.

table
    Pointer to the CFA table.

.. _`omap3isp_prev_csup`:

struct omap3isp_prev_csup
=========================

.. c:type:: struct omap3isp_prev_csup

    Chrominance Suppression

.. _`omap3isp_prev_csup.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_csup {
        __u8 gain;
        __u8 thres;
        __u8 hypf_en;
    }

.. _`omap3isp_prev_csup.members`:

Members
-------

gain
    Gain.

thres
    Threshold.

hypf_en
    Flag to enable/disable the High Pass Filter.

.. _`omap3isp_prev_wbal`:

struct omap3isp_prev_wbal
=========================

.. c:type:: struct omap3isp_prev_wbal

    White Balance

.. _`omap3isp_prev_wbal.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_wbal {
        __u16 dgain;
        __u8 coef3;
        __u8 coef2;
        __u8 coef1;
        __u8 coef0;
    }

.. _`omap3isp_prev_wbal.members`:

Members
-------

dgain
    Digital gain (U10Q8).

coef3
    White balance gain - COEF 3 (U8Q5).

coef2
    White balance gain - COEF 2 (U8Q5).

coef1
    White balance gain - COEF 1 (U8Q5).

coef0
    White balance gain - COEF 0 (U8Q5).

.. _`omap3isp_prev_blkadj`:

struct omap3isp_prev_blkadj
===========================

.. c:type:: struct omap3isp_prev_blkadj

    Black Level Adjustment

.. _`omap3isp_prev_blkadj.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_blkadj {
        __u8 red;
        __u8 green;
        __u8 blue;
    }

.. _`omap3isp_prev_blkadj.members`:

Members
-------

red
    Black level offset adjustment for Red in 2's complement format

green
    Black level offset adjustment for Green in 2's complement format

blue
    Black level offset adjustment for Blue in 2's complement format

.. _`omap3isp_prev_rgbtorgb`:

struct omap3isp_prev_rgbtorgb
=============================

.. c:type:: struct omap3isp_prev_rgbtorgb

    RGB to RGB Blending

.. _`omap3isp_prev_rgbtorgb.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_rgbtorgb {
        __u16 matrix[OMAP3ISP_RGB_MAX][OMAP3ISP_RGB_MAX];
        __u16 offset[OMAP3ISP_RGB_MAX];
    }

.. _`omap3isp_prev_rgbtorgb.members`:

Members
-------

matrix
    Blending values(S12Q8 format)
    [RR] [GR] [BR]
    [RG] [GG] [BG]
    [RB] [GB] [BB]

offset
    Blending offset value for R,G,B in 2's complement integer format.

.. _`omap3isp_prev_csc`:

struct omap3isp_prev_csc
========================

.. c:type:: struct omap3isp_prev_csc

    Color Space Conversion from RGB-YCbYCr

.. _`omap3isp_prev_csc.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_csc {
        __u16 matrix[OMAP3ISP_RGB_MAX][OMAP3ISP_RGB_MAX];
        __s16 offset[OMAP3ISP_RGB_MAX];
    }

.. _`omap3isp_prev_csc.members`:

Members
-------

matrix
    Color space conversion coefficients(S10Q8)
    [CSCRY]  [CSCGY]  [CSCBY]
    [CSCRCB] [CSCGCB] [CSCBCB]
    [CSCRCR] [CSCGCR] [CSCBCR]

offset
    CSC offset values for Y offset, CB offset and CR offset respectively

.. _`omap3isp_prev_yclimit`:

struct omap3isp_prev_yclimit
============================

.. c:type:: struct omap3isp_prev_yclimit

    Y, C Value Limit

.. _`omap3isp_prev_yclimit.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_yclimit {
        __u8 minC;
        __u8 maxC;
        __u8 minY;
        __u8 maxY;
    }

.. _`omap3isp_prev_yclimit.members`:

Members
-------

minC
    Minimum C value

maxC
    Maximum C value

minY
    Minimum Y value

maxY
    Maximum Y value

.. _`omap3isp_prev_dcor`:

struct omap3isp_prev_dcor
=========================

.. c:type:: struct omap3isp_prev_dcor

    Defect correction

.. _`omap3isp_prev_dcor.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_dcor {
        __u8 couplet_mode_en;
        __u32 detect_correct[OMAP3ISP_PREV_DETECT_CORRECT_CHANNELS];
    }

.. _`omap3isp_prev_dcor.members`:

Members
-------

couplet_mode_en
    Flag to enable or disable the couplet dc Correction in NF

detect_correct
    Thresholds for correction bit 0:10 detect 16:25 correct

.. _`omap3isp_prev_nf`:

struct omap3isp_prev_nf
=======================

.. c:type:: struct omap3isp_prev_nf

    Noise Filter

.. _`omap3isp_prev_nf.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_nf {
        __u8 spread;
        __u32 table[OMAP3ISP_PREV_NF_TBL_SIZE];
    }

.. _`omap3isp_prev_nf.members`:

Members
-------

spread
    Spread value to be used in Noise Filter

table
    Pointer to the Noise Filter table

.. _`omap3isp_prev_gtables`:

struct omap3isp_prev_gtables
============================

.. c:type:: struct omap3isp_prev_gtables

    Gamma correction tables

.. _`omap3isp_prev_gtables.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_gtables {
        __u32 red[OMAP3ISP_PREV_GAMMA_TBL_SIZE];
        __u32 green[OMAP3ISP_PREV_GAMMA_TBL_SIZE];
        __u32 blue[OMAP3ISP_PREV_GAMMA_TBL_SIZE];
    }

.. _`omap3isp_prev_gtables.members`:

Members
-------

red
    Array for red gamma table.

green
    Array for green gamma table.

blue
    Array for blue gamma table.

.. _`omap3isp_prev_luma`:

struct omap3isp_prev_luma
=========================

.. c:type:: struct omap3isp_prev_luma

    Luma enhancement

.. _`omap3isp_prev_luma.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_luma {
        __u32 table[OMAP3ISP_PREV_YENH_TBL_SIZE];
    }

.. _`omap3isp_prev_luma.members`:

Members
-------

table
    Array for luma enhancement table.

.. _`omap3isp_prev_update_config`:

struct omap3isp_prev_update_config
==================================

.. c:type:: struct omap3isp_prev_update_config

    Preview engine configuration (user)

.. _`omap3isp_prev_update_config.definition`:

Definition
----------

.. code-block:: c

    struct omap3isp_prev_update_config {
        __u32 update;
        __u32 flag;
        __u32 shading_shift;
        struct omap3isp_prev_luma __user *luma;
        struct omap3isp_prev_hmed __user *hmed;
        struct omap3isp_prev_cfa __user *cfa;
        struct omap3isp_prev_csup __user *csup;
        struct omap3isp_prev_wbal __user *wbal;
        struct omap3isp_prev_blkadj __user *blkadj;
        struct omap3isp_prev_rgbtorgb __user *rgb2rgb;
        struct omap3isp_prev_csc __user *csc;
        struct omap3isp_prev_yclimit __user *yclimit;
        struct omap3isp_prev_dcor __user *dcor;
        struct omap3isp_prev_nf __user *nf;
        struct omap3isp_prev_gtables __user *gamma;
    }

.. _`omap3isp_prev_update_config.members`:

Members
-------

update
    Specifies which ISP Preview registers should be updated.

flag
    Specifies which ISP Preview functions should be enabled.

shading_shift
    3bit value of shift used in shading compensation.

luma
    Pointer to luma enhancement structure.

hmed
    Pointer to structure containing the odd and even distance.
    between the pixels in the image along with the filter threshold.

cfa
    Pointer to structure containing the CFA interpolation table, CFA.
    format in the image, vertical and horizontal gradient threshold.

csup
    Pointer to Structure for Chrominance Suppression coefficients.

wbal
    Pointer to structure for White Balance.

blkadj
    Pointer to structure for Black Adjustment.

rgb2rgb
    Pointer to structure for RGB to RGB Blending.

csc
    Pointer to structure for Color Space Conversion from RGB-YCbYCr.

yclimit
    Pointer to structure for Y, C Value Limit.

dcor
    Pointer to structure for defect correction.

nf
    Pointer to structure for Noise Filter

gamma
    Pointer to gamma structure.

.. This file was automatic generated / don't edit.

