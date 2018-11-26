.. -*- coding: utf-8; mode: rst -*-
.. src-file: sound/drivers/vx/vx_cmd.h

.. _`vx_set_pipe_cmd_params`:

vx_set_pipe_cmd_params
======================

.. c:function:: void vx_set_pipe_cmd_params(struct vx_rmh *rmh, int is_capture, int param1, int param2)

    fill first command word for pipe commands

    :param rmh:
        the rmh to be modified
    :type rmh: struct vx_rmh \*

    :param is_capture:
        0 = playback, 1 = capture operation
    :type is_capture: int

    :param param1:
        first pipe-parameter
    :type param1: int

    :param param2:
        second pipe-parameter
    :type param2: int

.. _`vx_set_stream_cmd_params`:

vx_set_stream_cmd_params
========================

.. c:function:: void vx_set_stream_cmd_params(struct vx_rmh *rmh, int is_capture, int pipe)

    fill first command word for stream commands

    :param rmh:
        the rmh to be modified
    :type rmh: struct vx_rmh \*

    :param is_capture:
        0 = playback, 1 = capture operation
    :type is_capture: int

    :param pipe:
        the pipe index (zero-based)
    :type pipe: int

.. This file was automatic generated / don't edit.

