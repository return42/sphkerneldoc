.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/scu_completion_codes.h

.. _`scu_completion_type_shift`:

SCU_COMPLETION_TYPE_SHIFT
=========================

.. c:function::  SCU_COMPLETION_TYPE_SHIFT()

    codes.

.. _`scu_completion_type_shift.description`:

Description
-----------



.. _`scu_completion_type`:

SCU_COMPLETION_TYPE
===================

.. c:function::  SCU_COMPLETION_TYPE( type)

    :param  type:
        *undescribed*

.. _`scu_completion_type.description`:

Description
-----------

This macro constructs an SCU completion type

.. _`scu_completion_type_task`:

SCU_COMPLETION_TYPE_TASK
========================

.. c:function::  SCU_COMPLETION_TYPE_TASK()

.. _`scu_completion_type_task.description`:

Description
-----------

These macros contain the SCU completion types SCU_COMPLETION_TYPE

.. _`scu_get_completion_type`:

SCU_GET_COMPLETION_TYPE
=======================

.. c:function::  SCU_GET_COMPLETION_TYPE( completion_code)

    :param  completion_code:
        *undescribed*

.. _`scu_get_completion_type.description`:

Description
-----------

This macro returns the SCU completion type.

.. _`scu_get_completion_status`:

SCU_GET_COMPLETION_STATUS
=========================

.. c:function::  SCU_GET_COMPLETION_STATUS( completion_code)

    :param  completion_code:
        *undescribed*

.. _`scu_get_completion_status.description`:

Description
-----------

This macro returns the SCU completion status.

.. _`scu_get_completion_tl_status`:

SCU_GET_COMPLETION_TL_STATUS
============================

.. c:function::  SCU_GET_COMPLETION_TL_STATUS( completion_code)

    :param  completion_code:
        *undescribed*

.. _`scu_get_completion_tl_status.description`:

Description
-----------

This macro returns the transport layer completion status.

.. _`scu_make_completion_status`:

SCU_MAKE_COMPLETION_STATUS
==========================

.. c:function::  SCU_MAKE_COMPLETION_STATUS( completion_code)

    :param  completion_code:
        *undescribed*

.. _`scu_make_completion_status.description`:

Description
-----------

This macro takes a completion code and performs the shift and mask
operations to turn it into a completion code that can be compared to a
SCU_GET_COMPLETION_TL_STATUS.

.. _`scu_normalize_completion_status`:

SCU_NORMALIZE_COMPLETION_STATUS
===============================

.. c:function::  SCU_NORMALIZE_COMPLETION_STATUS( completion_code)

    :param  completion_code:
        *undescribed*

.. _`scu_normalize_completion_status.description`:

Description
-----------

This macro takes a SCU_GET_COMPLETION_TL_STATUS and normalizes it for a
return code.

.. _`scu_get_completion_sdma_status`:

SCU_GET_COMPLETION_SDMA_STATUS
==============================

.. c:function::  SCU_GET_COMPLETION_SDMA_STATUS( completion_code)

    :param  completion_code:
        *undescribed*

.. _`scu_get_completion_sdma_status.description`:

Description
-----------

This macro returns the SDMA completion status.

.. _`scu_get_completion_peg`:

SCU_GET_COMPLETION_PEG
======================

.. c:function::  SCU_GET_COMPLETION_PEG( completion_code)

    :param  completion_code:
        *undescribed*

.. _`scu_get_completion_peg.description`:

Description
-----------

This macro returns the Protocol Engine Group from the completion code.

.. _`scu_get_completion_port`:

SCU_GET_COMPLETION_PORT
=======================

.. c:function::  SCU_GET_COMPLETION_PORT( completion_code)

    :param  completion_code:
        *undescribed*

.. _`scu_get_completion_port.description`:

Description
-----------

This macro reuturns the logical port index from the completion code.

.. _`scu_get_protocol_engine_index`:

SCU_GET_PROTOCOL_ENGINE_INDEX
=============================

.. c:function::  SCU_GET_PROTOCOL_ENGINE_INDEX( completion_code)

    :param  completion_code:
        *undescribed*

.. _`scu_get_protocol_engine_index.description`:

Description
-----------

This macro returns the PE index from the completion code.

.. _`scu_get_completion_index`:

SCU_GET_COMPLETION_INDEX
========================

.. c:function::  SCU_GET_COMPLETION_INDEX( completion_code)

    :param  completion_code:
        *undescribed*

.. _`scu_get_completion_index.description`:

Description
-----------

This macro returns the index of the completion which is either a TCi or an
RNi depending on the completion type.

.. _`scu_get_frame_index`:

SCU_GET_FRAME_INDEX
===================

.. c:function::  SCU_GET_FRAME_INDEX( completion_code)

    :param  completion_code:
        *undescribed*

.. _`scu_get_frame_index.description`:

Description
-----------

This macro returns a normalized frame index from an unsolicited frame
completion.

.. _`scu_get_frame_error`:

SCU_GET_FRAME_ERROR
===================

.. c:function::  SCU_GET_FRAME_ERROR( completion_code)

    :param  completion_code:
        *undescribed*

.. _`scu_get_frame_error.description`:

Description
-----------

This macro returns a zero (0) value if there is no frame error otherwise it
returns non-zero (!0).

.. This file was automatic generated / don't edit.

