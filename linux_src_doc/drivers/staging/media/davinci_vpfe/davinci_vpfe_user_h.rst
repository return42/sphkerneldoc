.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/media/davinci_vpfe/davinci_vpfe_user.h

.. _`vpfe_isif_vdfc_table_size`:

VPFE_ISIF_VDFC_TABLE_SIZE
=========================

.. c:function::  VPFE_ISIF_VDFC_TABLE_SIZE()

.. _`vpfe_isif_csc_num_coeff`:

VPFE_ISIF_CSC_NUM_COEFF
=======================

.. c:function::  VPFE_ISIF_CSC_NUM_COEFF()

.. _`vpfe_ipipe_config`:

struct vpfe_ipipe_config
========================

.. c:type:: struct vpfe_ipipe_config

    IPIPE engine configuration (user)

.. _`vpfe_ipipe_config.definition`:

Definition
----------

.. code-block:: c

    struct vpfe_ipipe_config {
        __u32 flag;
        struct vpfe_ipipe_input_config __user *input_config;
        struct vpfe_ipipe_lutdpc __user *lutdpc;
        struct vpfe_ipipe_otfdpc __user *otfdpc;
        struct vpfe_ipipe_nf __user *nf1;
        struct vpfe_ipipe_nf __user *nf2;
        struct vpfe_ipipe_gic __user *gic;
        struct vpfe_ipipe_wb __user *wbal;
        struct vpfe_ipipe_cfa __user *cfa;
        struct vpfe_ipipe_rgb2rgb __user *rgb2rgb1;
        struct vpfe_ipipe_rgb2rgb __user *rgb2rgb2;
        struct vpfe_ipipe_gamma __user *gamma;
        struct vpfe_ipipe_3d_lut __user *lut;
        struct vpfe_ipipe_rgb2yuv __user *rgb2yuv;
        struct vpfe_ipipe_gbce __user *gbce;
        struct vpfe_ipipe_yuv422_conv __user *yuv422_conv;
        struct vpfe_ipipe_yee __user *yee;
        struct vpfe_ipipe_car __user *car;
        struct vpfe_ipipe_cgs __user *cgs;
    }

.. _`vpfe_ipipe_config.members`:

Members
-------

flag
    Specifies which ISP IPIPE functions should be enabled.

input_config
    Pointer to structure for ipipe configuration.

lutdpc
    Pointer to luma enhancement structure.

otfdpc
    Pointer to structure for defect correction.

nf1
    Pointer to structure for Noise Filter.

nf2
    Pointer to structure for Noise Filter.

gic
    Pointer to structure for Green Imbalance.

wbal
    Pointer to structure for White Balance.

cfa
    Pointer to structure containing the CFA interpolation.

rgb2rgb1
    Pointer to structure for RGB to RGB Blending.

rgb2rgb2
    Pointer to structure for RGB to RGB Blending.

gamma
    Pointer to gamma structure.

lut
    Pointer to structure for 3D LUT.

rgb2yuv
    Pointer to structure for RGB-YCbCr conversion.

gbce
    Pointer to structure for Global Brightness,Contrast Control.

yuv422_conv
    Pointer to structure for YUV 422 conversion.

yee
    Pointer to structure for Edge Enhancer.

car
    Pointer to structure for Chromatic Artifact Reduction.

cgs
    Pointer to structure for Chromatic Gain Suppression.

.. This file was automatic generated / don't edit.

