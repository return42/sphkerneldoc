.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/scsi/isci/scu_event_codes.h

.. _`scu_event_type_code_shift`:

SCU_EVENT_TYPE_CODE_SHIFT
=========================

.. c:function::  SCU_EVENT_TYPE_CODE_SHIFT()

.. _`scu_event_type_code_shift.description`:

Description
-----------



.. _`scu_event_type`:

SCU_EVENT_TYPE
==============

.. c:function::  SCU_EVENT_TYPE( type)

    :param type:
        *undescribed*
    :type type: 

.. _`scu_event_type.description`:

Description
-----------

This macro constructs an SCU event type from the type value.

.. _`scu_event_specific`:

SCU_EVENT_SPECIFIC
==================

.. c:function::  SCU_EVENT_SPECIFIC( code)

    :param code:
        *undescribed*
    :type code: 

.. _`scu_event_specific.description`:

Description
-----------

This macro constructs an SCU event specifier from the code value.

.. _`scu_event_message`:

SCU_EVENT_MESSAGE
=================

.. c:function::  SCU_EVENT_MESSAGE( type,  code)

    :param type:
        *undescribed*
    :type type: 

    :param code:
        *undescribed*
    :type code: 

.. _`scu_event_message.description`:

Description
-----------

This macro constructs a combines an SCU event type and SCU event specifier
from the type and code values.

.. _`scu_event_type_smu_command_error`:

SCU_EVENT_TYPE_SMU_COMMAND_ERROR
================================

.. c:function::  SCU_EVENT_TYPE_SMU_COMMAND_ERROR()

.. _`scu_event_type_smu_command_error.description`:

Description
-----------

SCU_EVENT_TYPES

.. _`scu_get_event_type`:

scu_get_event_type
==================

.. c:function::  scu_get_event_type( event_code)

    :param event_code:
        *undescribed*
    :type event_code: 

.. _`scu_get_event_type.description`:

Description
-----------

This macro returns the SCU event type from the event code.

.. _`scu_get_event_specifier`:

scu_get_event_specifier
=======================

.. c:function::  scu_get_event_specifier( event_code)

    :param event_code:
        *undescribed*
    :type event_code: 

.. _`scu_get_event_specifier.description`:

Description
-----------

This macro returns the SCU event specifier from the event code.

.. _`scu_get_event_code`:

scu_get_event_code
==================

.. c:function::  scu_get_event_code( event_code)

    :param event_code:
        *undescribed*
    :type event_code: 

.. _`scu_get_event_code.description`:

Description
-----------

This macro returns the combined SCU event type and SCU event specifier from
the event code.

.. This file was automatic generated / don't edit.

