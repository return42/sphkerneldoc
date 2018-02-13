.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/linux/zstd.h

.. _`zstd_errorcode`:

typedef ZSTD_ErrorCode
======================

.. c:type:: typedef ZSTD_ErrorCode

    zstd error codes

.. _`zstd_errorcode.description`:

Description
-----------

Functions that return size_t can be checked for errors using \ :c:func:`ZSTD_isError`\ 
and the ZSTD_ErrorCode can be extracted using \ :c:func:`ZSTD_getErrorCode`\ .

.. _`zstd_maxclevel`:

ZSTD_maxCLevel
==============

.. c:function:: int ZSTD_maxCLevel( void)

    maximum compression level available

    :param  void:
        no arguments

.. _`zstd_maxclevel.return`:

Return
------

Maximum compression level available.

.. _`zstd_compressbound`:

ZSTD_compressBound
==================

.. c:function:: size_t ZSTD_compressBound(size_t srcSize)

    maximum compressed size in worst case scenario

    :param size_t srcSize:
        The size of the data to compress.

.. _`zstd_compressbound.return`:

Return
------

The maximum compressed size in the worst case scenario.

.. _`zstd_iserror`:

ZSTD_isError
============

.. c:function:: unsigned int ZSTD_isError(size_t code)

    tells if a size_t function result is an error code

    :param size_t code:
        The function result to check for error.

.. _`zstd_iserror.return`:

Return
------

Non-zero iff the code is an error.

.. _`zstd_geterrorcode`:

ZSTD_getErrorCode
=================

.. c:function:: ZSTD_ErrorCode ZSTD_getErrorCode(size_t functionResult)

    translates an error function result to a ZSTD_ErrorCode

    :param size_t functionResult:
        The result of a function for which \ :c:func:`ZSTD_isError`\  is true.

.. _`zstd_geterrorcode.return`:

Return
------

The ZSTD_ErrorCode corresponding to the functionResult or 0
if the functionResult isn't an error.

.. _`zstd_strategy`:

typedef ZSTD_strategy
=====================

.. c:type:: typedef ZSTD_strategy

    zstd compression search strategy

.. _`zstd_strategy.description`:

Description
-----------

From faster to stronger.

.. _`zstd_compressionparameters`:

typedef ZSTD_compressionParameters
==================================

.. c:type:: typedef ZSTD_compressionParameters

    zstd compression parameters

.. _`zstd_frameparameters`:

typedef ZSTD_frameParameters
============================

.. c:type:: typedef ZSTD_frameParameters

    zstd frame parameters

.. _`zstd_frameparameters.description`:

Description
-----------

The default value is all fields set to 0.

.. _`zstd_parameters`:

typedef ZSTD_parameters
=======================

.. c:type:: typedef ZSTD_parameters

    zstd parameters

.. _`zstd_getcparams`:

ZSTD_getCParams
===============

.. c:function:: ZSTD_compressionParameters ZSTD_getCParams(int compressionLevel, unsigned long long estimatedSrcSize, size_t dictSize)

    returns ZSTD_compressionParameters for selected level

    :param int compressionLevel:
        The compression level from 1 to \ :c:func:`ZSTD_maxCLevel`\ .

    :param unsigned long long estimatedSrcSize:
        The estimated source size to compress or 0 if unknown.

    :param size_t dictSize:
        The dictionary size or 0 if a dictionary isn't being used.

.. _`zstd_getcparams.return`:

Return
------

The selected ZSTD_compressionParameters.

.. _`zstd_getparams`:

ZSTD_getParams
==============

.. c:function:: ZSTD_parameters ZSTD_getParams(int compressionLevel, unsigned long long estimatedSrcSize, size_t dictSize)

    returns ZSTD_parameters for selected level

    :param int compressionLevel:
        The compression level from 1 to \ :c:func:`ZSTD_maxCLevel`\ .

    :param unsigned long long estimatedSrcSize:
        The estimated source size to compress or 0 if unknown.

    :param size_t dictSize:
        The dictionary size or 0 if a dictionary isn't being used.

.. _`zstd_getparams.description`:

Description
-----------

The same as \ :c:func:`ZSTD_getCParams`\  except also selects the default frame
parameters (all zero).

.. _`zstd_getparams.return`:

Return
------

The selected ZSTD_parameters.

.. _`zstd_cctxworkspacebound`:

ZSTD_CCtxWorkspaceBound
=======================

.. c:function:: size_t ZSTD_CCtxWorkspaceBound(ZSTD_compressionParameters cParams)

    amount of memory needed to initialize a ZSTD_CCtx

    :param ZSTD_compressionParameters cParams:
        The compression parameters to be used for compression.

.. _`zstd_cctxworkspacebound.description`:

Description
-----------

If multiple compression parameters might be used, the caller must call
\ :c:func:`ZSTD_CCtxWorkspaceBound`\  for each set of parameters and use the maximum
size.

.. _`zstd_cctxworkspacebound.return`:

Return
------

A lower bound on the size of the workspace that is passed to
\ :c:func:`ZSTD_initCCtx`\ .

.. _`zstd_cctx`:

typedef ZSTD_CCtx
=================

.. c:type:: typedef ZSTD_CCtx

    the zstd compression context

.. _`zstd_cctx.description`:

Description
-----------

When compressing many times it is recommended to allocate a context just once
and reuse it for each successive compression operation.

.. _`zstd_initcctx`:

ZSTD_initCCtx
=============

.. c:function:: ZSTD_CCtx *ZSTD_initCCtx(void *workspace, size_t workspaceSize)

    initialize a zstd compression context

    :param void \*workspace:
        The workspace to emplace the context into. It must outlive
        the returned context.

    :param size_t workspaceSize:
        The size of workspace. Use \ :c:func:`ZSTD_CCtxWorkspaceBound`\  to
        determine how large the workspace must be.

.. _`zstd_initcctx.return`:

Return
------

A compression context emplaced into workspace.

.. _`zstd_compresscctx`:

ZSTD_compressCCtx
=================

.. c:function:: size_t ZSTD_compressCCtx(ZSTD_CCtx *ctx, void *dst, size_t dstCapacity, const void *src, size_t srcSize, ZSTD_parameters params)

    compress src into dst

    :param ZSTD_CCtx \*ctx:
        The context. Must have been initialized with a workspace at
        least as large as ZSTD_CCtxWorkspaceBound(params.cParams).

    :param void \*dst:
        The buffer to compress src into.

    :param size_t dstCapacity:
        The size of the destination buffer. May be any size, but
        ZSTD_compressBound(srcSize) is guaranteed to be large enough.

    :param const void \*src:
        The data to compress.

    :param size_t srcSize:
        The size of the data to compress.

    :param ZSTD_parameters params:
        The parameters to use for compression. See \ :c:func:`ZSTD_getParams`\ .

.. _`zstd_compresscctx.return`:

Return
------

The compressed size or an error, which can be checked using
\ :c:func:`ZSTD_isError`\ .

.. _`zstd_dctxworkspacebound`:

ZSTD_DCtxWorkspaceBound
=======================

.. c:function:: size_t ZSTD_DCtxWorkspaceBound( void)

    amount of memory needed to initialize a ZSTD_DCtx

    :param  void:
        no arguments

.. _`zstd_dctxworkspacebound.return`:

Return
------

A lower bound on the size of the workspace that is passed to
\ :c:func:`ZSTD_initDCtx`\ .

.. _`zstd_dctx`:

typedef ZSTD_DCtx
=================

.. c:type:: typedef ZSTD_DCtx

    the zstd decompression context

.. _`zstd_dctx.description`:

Description
-----------

When decompressing many times it is recommended to allocate a context just
once and reuse it for each successive decompression operation.

.. _`zstd_initdctx`:

ZSTD_initDCtx
=============

.. c:function:: ZSTD_DCtx *ZSTD_initDCtx(void *workspace, size_t workspaceSize)

    initialize a zstd decompression context

    :param void \*workspace:
        The workspace to emplace the context into. It must outlive
        the returned context.

    :param size_t workspaceSize:
        The size of workspace. Use \ :c:func:`ZSTD_DCtxWorkspaceBound`\  to
        determine how large the workspace must be.

.. _`zstd_initdctx.return`:

Return
------

A decompression context emplaced into workspace.

.. _`zstd_decompressdctx`:

ZSTD_decompressDCtx
===================

.. c:function:: size_t ZSTD_decompressDCtx(ZSTD_DCtx *ctx, void *dst, size_t dstCapacity, const void *src, size_t srcSize)

    decompress zstd compressed src into dst

    :param ZSTD_DCtx \*ctx:
        The decompression context.

    :param void \*dst:
        The buffer to decompress src into.

    :param size_t dstCapacity:
        The size of the destination buffer. Must be at least as large
        as the decompressed size. If the caller cannot upper bound the
        decompressed size, then it's better to use the streaming API.

    :param const void \*src:
        The zstd compressed data to decompress. Multiple concatenated
        frames and skippable frames are allowed.

    :param size_t srcSize:
        The exact size of the data to decompress.

.. _`zstd_decompressdctx.return`:

Return
------

The decompressed size or an error, which can be checked using
\ :c:func:`ZSTD_isError`\ .

.. _`zstd_compress_usingdict`:

ZSTD_compress_usingDict
=======================

.. c:function:: size_t ZSTD_compress_usingDict(ZSTD_CCtx *ctx, void *dst, size_t dstCapacity, const void *src, size_t srcSize, const void *dict, size_t dictSize, ZSTD_parameters params)

    compress src into dst using a dictionary

    :param ZSTD_CCtx \*ctx:
        The context. Must have been initialized with a workspace at
        least as large as ZSTD_CCtxWorkspaceBound(params.cParams).

    :param void \*dst:
        The buffer to compress src into.

    :param size_t dstCapacity:
        The size of the destination buffer. May be any size, but
        ZSTD_compressBound(srcSize) is guaranteed to be large enough.

    :param const void \*src:
        The data to compress.

    :param size_t srcSize:
        The size of the data to compress.

    :param const void \*dict:
        The dictionary to use for compression.

    :param size_t dictSize:
        The size of the dictionary.

    :param ZSTD_parameters params:
        The parameters to use for compression. See \ :c:func:`ZSTD_getParams`\ .

.. _`zstd_compress_usingdict.description`:

Description
-----------

Compression using a predefined dictionary. The same dictionary must be used
during decompression.

.. _`zstd_compress_usingdict.return`:

Return
------

The compressed size or an error, which can be checked using
\ :c:func:`ZSTD_isError`\ .

.. _`zstd_decompress_usingdict`:

ZSTD_decompress_usingDict
=========================

.. c:function:: size_t ZSTD_decompress_usingDict(ZSTD_DCtx *ctx, void *dst, size_t dstCapacity, const void *src, size_t srcSize, const void *dict, size_t dictSize)

    decompress src into dst using a dictionary

    :param ZSTD_DCtx \*ctx:
        The decompression context.

    :param void \*dst:
        The buffer to decompress src into.

    :param size_t dstCapacity:
        The size of the destination buffer. Must be at least as large
        as the decompressed size. If the caller cannot upper bound the
        decompressed size, then it's better to use the streaming API.

    :param const void \*src:
        The zstd compressed data to decompress. Multiple concatenated
        frames and skippable frames are allowed.

    :param size_t srcSize:
        The exact size of the data to decompress.

    :param const void \*dict:
        The dictionary to use for decompression. The same dictionary
        must've been used to compress the data.

    :param size_t dictSize:
        The size of the dictionary.

.. _`zstd_decompress_usingdict.return`:

Return
------

The decompressed size or an error, which can be checked using
\ :c:func:`ZSTD_isError`\ .

.. _`zstd_cdictworkspacebound`:

ZSTD_CDictWorkspaceBound
========================

.. c:function:: size_t ZSTD_CDictWorkspaceBound(ZSTD_compressionParameters cParams)

    memory needed to initialize a ZSTD_CDict

    :param ZSTD_compressionParameters cParams:
        The compression parameters to be used for compression.

.. _`zstd_cdictworkspacebound.return`:

Return
------

A lower bound on the size of the workspace that is passed to
\ :c:func:`ZSTD_initCDict`\ .

.. _`zstd_cdict`:

typedef ZSTD_CDict
==================

.. c:type:: typedef ZSTD_CDict

    a digested dictionary to be used for compression

.. _`zstd_initcdict`:

ZSTD_initCDict
==============

.. c:function:: ZSTD_CDict *ZSTD_initCDict(const void *dictBuffer, size_t dictSize, ZSTD_parameters params, void *workspace, size_t workspaceSize)

    initialize a digested dictionary for compression

    :param const void \*dictBuffer:
        The dictionary to digest. The buffer is referenced by the
        ZSTD_CDict so it must outlive the returned ZSTD_CDict.

    :param size_t dictSize:
        The size of the dictionary.

    :param ZSTD_parameters params:
        The parameters to use for compression. See \ :c:func:`ZSTD_getParams`\ .

    :param void \*workspace:
        The workspace. It must outlive the returned ZSTD_CDict.

    :param size_t workspaceSize:
        The workspace size. Must be at least
        ZSTD_CDictWorkspaceBound(params.cParams).

.. _`zstd_initcdict.description`:

Description
-----------

When compressing multiple messages / blocks with the same dictionary it is
recommended to load it just once. The ZSTD_CDict merely references the
dictBuffer, so it must outlive the returned ZSTD_CDict.

.. _`zstd_initcdict.return`:

Return
------

The digested dictionary emplaced into workspace.

.. _`zstd_compress_usingcdict`:

ZSTD_compress_usingCDict
========================

.. c:function:: size_t ZSTD_compress_usingCDict(ZSTD_CCtx *cctx, void *dst, size_t dstCapacity, const void *src, size_t srcSize, const ZSTD_CDict *cdict)

    compress src into dst using a ZSTD_CDict

    :param ZSTD_CCtx \*cctx:
        *undescribed*

    :param void \*dst:
        The buffer to compress src into.

    :param size_t dstCapacity:
        The size of the destination buffer. May be any size, but
        ZSTD_compressBound(srcSize) is guaranteed to be large enough.

    :param const void \*src:
        The data to compress.

    :param size_t srcSize:
        The size of the data to compress.

    :param const ZSTD_CDict \*cdict:
        The digested dictionary to use for compression.

.. _`zstd_compress_usingcdict.description`:

Description
-----------

Compression using a digested dictionary. The same dictionary must be used
during decompression.

.. _`zstd_compress_usingcdict.return`:

Return
------

The compressed size or an error, which can be checked using
\ :c:func:`ZSTD_isError`\ .

.. _`zstd_ddictworkspacebound`:

ZSTD_DDictWorkspaceBound
========================

.. c:function:: size_t ZSTD_DDictWorkspaceBound( void)

    memory needed to initialize a ZSTD_DDict

    :param  void:
        no arguments

.. _`zstd_ddictworkspacebound.return`:

Return
------

A lower bound on the size of the workspace that is passed to
\ :c:func:`ZSTD_initDDict`\ .

.. _`zstd_ddict`:

typedef ZSTD_DDict
==================

.. c:type:: typedef ZSTD_DDict

    a digested dictionary to be used for decompression

.. _`zstd_initddict`:

ZSTD_initDDict
==============

.. c:function:: ZSTD_DDict *ZSTD_initDDict(const void *dictBuffer, size_t dictSize, void *workspace, size_t workspaceSize)

    initialize a digested dictionary for decompression

    :param const void \*dictBuffer:
        The dictionary to digest. The buffer is referenced by the
        ZSTD_DDict so it must outlive the returned ZSTD_DDict.

    :param size_t dictSize:
        The size of the dictionary.

    :param void \*workspace:
        The workspace. It must outlive the returned ZSTD_DDict.

    :param size_t workspaceSize:
        The workspace size. Must be at least
        \ :c:func:`ZSTD_DDictWorkspaceBound`\ .

.. _`zstd_initddict.description`:

Description
-----------

When decompressing multiple messages / blocks with the same dictionary it is
recommended to load it just once. The ZSTD_DDict merely references the
dictBuffer, so it must outlive the returned ZSTD_DDict.

.. _`zstd_initddict.return`:

Return
------

The digested dictionary emplaced into workspace.

.. _`zstd_decompress_usingddict`:

ZSTD_decompress_usingDDict
==========================

.. c:function:: size_t ZSTD_decompress_usingDDict(ZSTD_DCtx *dctx, void *dst, size_t dstCapacity, const void *src, size_t srcSize, const ZSTD_DDict *ddict)

    decompress src into dst using a ZSTD_DDict

    :param ZSTD_DCtx \*dctx:
        *undescribed*

    :param void \*dst:
        The buffer to decompress src into.

    :param size_t dstCapacity:
        The size of the destination buffer. Must be at least as large
        as the decompressed size. If the caller cannot upper bound the
        decompressed size, then it's better to use the streaming API.

    :param const void \*src:
        The zstd compressed data to decompress. Multiple concatenated
        frames and skippable frames are allowed.

    :param size_t srcSize:
        The exact size of the data to decompress.

    :param const ZSTD_DDict \*ddict:
        The digested dictionary to use for decompression. The same
        dictionary must've been used to compress the data.

.. _`zstd_decompress_usingddict.return`:

Return
------

The decompressed size or an error, which can be checked using
\ :c:func:`ZSTD_isError`\ .

.. _`zstd_inbuffer`:

typedef ZSTD_inBuffer
=====================

.. c:type:: typedef ZSTD_inBuffer

    input buffer for streaming

.. _`zstd_outbuffer`:

typedef ZSTD_outBuffer
======================

.. c:type:: typedef ZSTD_outBuffer

    output buffer for streaming

.. _`zstd_cstreamworkspacebound`:

ZSTD_CStreamWorkspaceBound
==========================

.. c:function:: size_t ZSTD_CStreamWorkspaceBound(ZSTD_compressionParameters cParams)

    memory needed to initialize a ZSTD_CStream

    :param ZSTD_compressionParameters cParams:
        The compression parameters to be used for compression.

.. _`zstd_cstreamworkspacebound.return`:

Return
------

A lower bound on the size of the workspace that is passed to
\ :c:func:`ZSTD_initCStream`\  and \ :c:func:`ZSTD_initCStream_usingCDict`\ .

.. _`zstd_cstream`:

typedef ZSTD_CStream
====================

.. c:type:: typedef ZSTD_CStream

    the zstd streaming compression context

.. _`zstd_initcstream`:

ZSTD_initCStream
================

.. c:function:: ZSTD_CStream *ZSTD_initCStream(ZSTD_parameters params, unsigned long long pledgedSrcSize, void *workspace, size_t workspaceSize)

    initialize a zstd streaming compression context

    :param ZSTD_parameters params:
        The zstd compression parameters.

    :param unsigned long long pledgedSrcSize:
        If params.fParams.contentSizeFlag == 1 then the caller must
        pass the source size (zero means empty source). Otherwise,
        the caller may optionally pass the source size, or zero if
        unknown.

    :param void \*workspace:
        The workspace to emplace the context into. It must outlive
        the returned context.

    :param size_t workspaceSize:
        The size of workspace.
        Use ZSTD_CStreamWorkspaceBound(params.cParams) to determine
        how large the workspace must be.

.. _`zstd_initcstream.return`:

Return
------

The zstd streaming compression context.

.. _`zstd_initcstream_usingcdict`:

ZSTD_initCStream_usingCDict
===========================

.. c:function:: ZSTD_CStream *ZSTD_initCStream_usingCDict(const ZSTD_CDict *cdict, unsigned long long pledgedSrcSize, void *workspace, size_t workspaceSize)

    initialize a streaming compression context

    :param const ZSTD_CDict \*cdict:
        The digested dictionary to use for compression.

    :param unsigned long long pledgedSrcSize:
        Optionally the source size, or zero if unknown.

    :param void \*workspace:
        The workspace to emplace the context into. It must outlive
        the returned context.

    :param size_t workspaceSize:
        The size of workspace. Call \ :c:func:`ZSTD_CStreamWorkspaceBound`\ 
        with the cParams used to initialize the cdict to determine
        how large the workspace must be.

.. _`zstd_initcstream_usingcdict.return`:

Return
------

The zstd streaming compression context.

.. _`zstd_resetcstream`:

ZSTD_resetCStream
=================

.. c:function:: size_t ZSTD_resetCStream(ZSTD_CStream *zcs, unsigned long long pledgedSrcSize)

    reset the context using parameters from creation

    :param ZSTD_CStream \*zcs:
        The zstd streaming compression context to reset.

    :param unsigned long long pledgedSrcSize:
        Optionally the source size, or zero if unknown.

.. _`zstd_resetcstream.description`:

Description
-----------

Resets the context using the parameters from creation. Skips dictionary
loading, since it can be reused. If \`pledgedSrcSize\` is non-zero the frame
content size is always written into the frame header.

.. _`zstd_resetcstream.return`:

Return
------

Zero or an error, which can be checked using \ :c:func:`ZSTD_isError`\ .

.. _`zstd_compressstream`:

ZSTD_compressStream
===================

.. c:function:: size_t ZSTD_compressStream(ZSTD_CStream *zcs, ZSTD_outBuffer *output, ZSTD_inBuffer *input)

    streaming compress some of input into output

    :param ZSTD_CStream \*zcs:
        The zstd streaming compression context.

    :param ZSTD_outBuffer \*output:
        Destination buffer. \`output->pos\` is updated to indicate how much
        compressed data was written.

    :param ZSTD_inBuffer \*input:
        Source buffer. \`input->pos\` is updated to indicate how much data was
        read. Note that it may not consume the entire input, in which case
        \`input->pos < input->size\`, and it's up to the caller to present
        remaining data again.

.. _`zstd_compressstream.description`:

Description
-----------

The \`input\` and \`output\` buffers may be any size. Guaranteed to make some
forward progress if \`input\` and \`output\` are not empty.

.. _`zstd_compressstream.return`:

Return
------

A hint for the number of bytes to use as the input for the next
function call or an error, which can be checked using
\ :c:func:`ZSTD_isError`\ .

.. _`zstd_flushstream`:

ZSTD_flushStream
================

.. c:function:: size_t ZSTD_flushStream(ZSTD_CStream *zcs, ZSTD_outBuffer *output)

    flush internal buffers into output

    :param ZSTD_CStream \*zcs:
        The zstd streaming compression context.

    :param ZSTD_outBuffer \*output:
        Destination buffer. \`output->pos\` is updated to indicate how much
        compressed data was written.

.. _`zstd_flushstream.description`:

Description
-----------

\ :c:func:`ZSTD_flushStream`\  must be called until it returns 0, meaning all the data
has been flushed. Since \ :c:func:`ZSTD_flushStream`\  causes a block to be ended,
calling it too often will degrade the compression ratio.

.. _`zstd_flushstream.return`:

Return
------

The number of bytes still present within internal buffers or an
error, which can be checked using \ :c:func:`ZSTD_isError`\ .

.. _`zstd_endstream`:

ZSTD_endStream
==============

.. c:function:: size_t ZSTD_endStream(ZSTD_CStream *zcs, ZSTD_outBuffer *output)

    flush internal buffers into output and end the frame

    :param ZSTD_CStream \*zcs:
        The zstd streaming compression context.

    :param ZSTD_outBuffer \*output:
        Destination buffer. \`output->pos\` is updated to indicate how much
        compressed data was written.

.. _`zstd_endstream.description`:

Description
-----------

\ :c:func:`ZSTD_endStream`\  must be called until it returns 0, meaning all the data has
been flushed and the frame epilogue has been written.

.. _`zstd_endstream.return`:

Return
------

The number of bytes still present within internal buffers or an
error, which can be checked using \ :c:func:`ZSTD_isError`\ .

.. _`zstd_cstreaminsize`:

ZSTD_CStreamInSize
==================

.. c:function:: size_t ZSTD_CStreamInSize( void)

    recommended size for the input buffer

    :param  void:
        no arguments

.. _`zstd_cstreaminsize.return`:

Return
------

The recommended size for the input buffer.

.. _`zstd_cstreamoutsize`:

ZSTD_CStreamOutSize
===================

.. c:function:: size_t ZSTD_CStreamOutSize( void)

    recommended size for the output buffer

    :param  void:
        no arguments

.. _`zstd_cstreamoutsize.description`:

Description
-----------

When the output buffer is at least this large, it is guaranteed to be large
enough to flush at least one complete compressed block.

.. _`zstd_cstreamoutsize.return`:

Return
------

The recommended size for the output buffer.

.. _`zstd_dstreamworkspacebound`:

ZSTD_DStreamWorkspaceBound
==========================

.. c:function:: size_t ZSTD_DStreamWorkspaceBound(size_t maxWindowSize)

    memory needed to initialize a ZSTD_DStream

    :param size_t maxWindowSize:
        The maximum window size allowed for compressed frames.

.. _`zstd_dstreamworkspacebound.return`:

Return
------

A lower bound on the size of the workspace that is passed to
\ :c:func:`ZSTD_initDStream`\  and \ :c:func:`ZSTD_initDStream_usingDDict`\ .

.. _`zstd_dstream`:

typedef ZSTD_DStream
====================

.. c:type:: typedef ZSTD_DStream

    the zstd streaming decompression context

.. _`zstd_initdstream`:

ZSTD_initDStream
================

.. c:function:: ZSTD_DStream *ZSTD_initDStream(size_t maxWindowSize, void *workspace, size_t workspaceSize)

    initialize a zstd streaming decompression context

    :param size_t maxWindowSize:
        The maximum window size allowed for compressed frames.

    :param void \*workspace:
        The workspace to emplace the context into. It must outlive
        the returned context.

    :param size_t workspaceSize:
        The size of workspace.
        Use ZSTD_DStreamWorkspaceBound(maxWindowSize) to determine
        how large the workspace must be.

.. _`zstd_initdstream.return`:

Return
------

The zstd streaming decompression context.

.. _`zstd_initdstream_usingddict`:

ZSTD_initDStream_usingDDict
===========================

.. c:function:: ZSTD_DStream *ZSTD_initDStream_usingDDict(size_t maxWindowSize, const ZSTD_DDict *ddict, void *workspace, size_t workspaceSize)

    initialize streaming decompression context

    :param size_t maxWindowSize:
        The maximum window size allowed for compressed frames.

    :param const ZSTD_DDict \*ddict:
        The digested dictionary to use for decompression.

    :param void \*workspace:
        The workspace to emplace the context into. It must outlive
        the returned context.

    :param size_t workspaceSize:
        The size of workspace.
        Use ZSTD_DStreamWorkspaceBound(maxWindowSize) to determine
        how large the workspace must be.

.. _`zstd_initdstream_usingddict.return`:

Return
------

The zstd streaming decompression context.

.. _`zstd_resetdstream`:

ZSTD_resetDStream
=================

.. c:function:: size_t ZSTD_resetDStream(ZSTD_DStream *zds)

    reset the context using parameters from creation

    :param ZSTD_DStream \*zds:
        The zstd streaming decompression context to reset.

.. _`zstd_resetdstream.description`:

Description
-----------

Resets the context using the parameters from creation. Skips dictionary
loading, since it can be reused.

.. _`zstd_resetdstream.return`:

Return
------

Zero or an error, which can be checked using \ :c:func:`ZSTD_isError`\ .

.. _`zstd_decompressstream`:

ZSTD_decompressStream
=====================

.. c:function:: size_t ZSTD_decompressStream(ZSTD_DStream *zds, ZSTD_outBuffer *output, ZSTD_inBuffer *input)

    streaming decompress some of input into output

    :param ZSTD_DStream \*zds:
        The zstd streaming decompression context.

    :param ZSTD_outBuffer \*output:
        Destination buffer. \`output.pos\` is updated to indicate how much
        decompressed data was written.

    :param ZSTD_inBuffer \*input:
        Source buffer. \`input.pos\` is updated to indicate how much data was
        read. Note that it may not consume the entire input, in which case
        \`input.pos < input.size\`, and it's up to the caller to present
        remaining data again.

.. _`zstd_decompressstream.description`:

Description
-----------

The \`input\` and \`output\` buffers may be any size. Guaranteed to make some
forward progress if \`input\` and \`output\` are not empty.
\ :c:func:`ZSTD_decompressStream`\  will not consume the last byte of the frame until
the entire frame is flushed.

.. _`zstd_decompressstream.return`:

Return
------

Returns 0 iff a frame is completely decoded and fully flushed.
Otherwise returns a hint for the number of bytes to use as the input
for the next function call or an error, which can be checked using
\ :c:func:`ZSTD_isError`\ . The size hint will never load more than the frame.

.. _`zstd_dstreaminsize`:

ZSTD_DStreamInSize
==================

.. c:function:: size_t ZSTD_DStreamInSize( void)

    recommended size for the input buffer

    :param  void:
        no arguments

.. _`zstd_dstreaminsize.return`:

Return
------

The recommended size for the input buffer.

.. _`zstd_dstreamoutsize`:

ZSTD_DStreamOutSize
===================

.. c:function:: size_t ZSTD_DStreamOutSize( void)

    recommended size for the output buffer

    :param  void:
        no arguments

.. _`zstd_dstreamoutsize.description`:

Description
-----------

When the output buffer is at least this large, it is guaranteed to be large
enough to flush at least one complete decompressed block.

.. _`zstd_dstreamoutsize.return`:

Return
------

The recommended size for the output buffer.

.. _`zstd_findframecompressedsize`:

ZSTD_findFrameCompressedSize
============================

.. c:function:: size_t ZSTD_findFrameCompressedSize(const void *src, size_t srcSize)

    returns the size of a compressed frame

    :param const void \*src:
        Source buffer. It should point to the start of a zstd encoded frame
        or a skippable frame.

    :param size_t srcSize:
        The size of the source buffer. It must be at least as large as the
        size of the frame.

.. _`zstd_findframecompressedsize.return`:

Return
------

The compressed size of the frame pointed to by \`src\` or an error,
which can be check with \ :c:func:`ZSTD_isError`\ .
Suitable to pass to \ :c:func:`ZSTD_decompress`\  or similar functions.

.. _`zstd_getframecontentsize`:

ZSTD_getFrameContentSize
========================

.. c:function:: unsigned long long ZSTD_getFrameContentSize(const void *src, size_t srcSize)

    returns the content size in a zstd frame header

    :param const void \*src:
        It should point to the start of a zstd encoded frame.

    :param size_t srcSize:
        The size of the source buffer. It must be at least as large as the
        frame header. \`ZSTD_frameHeaderSize_max\` is always large enough.

.. _`zstd_getframecontentsize.return`:

Return
------

The frame content size stored in the frame header if known.
\`ZSTD_CONTENTSIZE_UNKNOWN\` if the content size isn't stored in the
frame header. \`ZSTD_CONTENTSIZE_ERROR\` on invalid input.

.. _`zstd_finddecompressedsize`:

ZSTD_findDecompressedSize
=========================

.. c:function:: unsigned long long ZSTD_findDecompressedSize(const void *src, size_t srcSize)

    returns decompressed size of a series of frames

    :param const void \*src:
        It should point to the start of a series of zstd encoded and/or
        skippable frames.

    :param size_t srcSize:
        The exact size of the series of frames.

.. _`zstd_finddecompressedsize.description`:

Description
-----------

If any zstd encoded frame in the series doesn't have the frame content size
set, \`ZSTD_CONTENTSIZE_UNKNOWN\` is returned. But frame content size is always
set when using \ :c:func:`ZSTD_compress`\ . The decompressed size can be very large.
If the source is untrusted, the decompressed size could be wrong or
intentionally modified. Always ensure the result fits within the
application's authorized limits. \ :c:func:`ZSTD_findDecompressedSize`\  handles multiple
frames, and so it must traverse the input to read each frame header. This is
efficient as most of the data is skipped, however it does mean that all frame
data must be present and valid.

.. _`zstd_finddecompressedsize.return`:

Return
------

Decompressed size of all the data contained in the frames if known.
\`ZSTD_CONTENTSIZE_UNKNOWN\` if the decompressed size is unknown.
\`ZSTD_CONTENTSIZE_ERROR\` if an error occurred.

.. _`zstd_checkcparams`:

ZSTD_checkCParams
=================

.. c:function:: size_t ZSTD_checkCParams(ZSTD_compressionParameters cParams)

    ensure parameter values remain within authorized range

    :param ZSTD_compressionParameters cParams:
        The zstd compression parameters.

.. _`zstd_checkcparams.return`:

Return
------

Zero or an error, which can be checked using \ :c:func:`ZSTD_isError`\ .

.. _`zstd_adjustcparams`:

ZSTD_adjustCParams
==================

.. c:function:: ZSTD_compressionParameters ZSTD_adjustCParams(ZSTD_compressionParameters cParams, unsigned long long srcSize, size_t dictSize)

    optimize parameters for a given srcSize and dictSize

    :param ZSTD_compressionParameters cParams:
        *undescribed*

    :param unsigned long long srcSize:
        Optionally the estimated source size, or zero if unknown.

    :param size_t dictSize:
        Optionally the estimated dictionary size, or zero if unknown.

.. _`zstd_adjustcparams.return`:

Return
------

The optimized parameters.

.. _`zstd_isframe`:

ZSTD_isFrame
============

.. c:function:: unsigned int ZSTD_isFrame(const void *buffer, size_t size)

    returns true iff the buffer starts with a valid frame

    :param const void \*buffer:
        The source buffer to check.

    :param size_t size:
        The size of the source buffer, must be at least 4 bytes.

.. _`zstd_isframe.return`:

Return
------

True iff the buffer starts with a zstd or skippable frame identifier.

.. _`zstd_getdictid_fromdict`:

ZSTD_getDictID_fromDict
=======================

.. c:function:: unsigned int ZSTD_getDictID_fromDict(const void *dict, size_t dictSize)

    returns the dictionary id stored in a dictionary

    :param const void \*dict:
        The dictionary buffer.

    :param size_t dictSize:
        The size of the dictionary buffer.

.. _`zstd_getdictid_fromdict.return`:

Return
------

The dictionary id stored within the dictionary or 0 if the
dictionary is not a zstd dictionary. If it returns 0 the
dictionary can still be loaded as a content-only dictionary.

.. _`zstd_getdictid_fromddict`:

ZSTD_getDictID_fromDDict
========================

.. c:function:: unsigned int ZSTD_getDictID_fromDDict(const ZSTD_DDict *ddict)

    returns the dictionary id stored in a ZSTD_DDict

    :param const ZSTD_DDict \*ddict:
        The ddict to find the id of.

.. _`zstd_getdictid_fromddict.return`:

Return
------

The dictionary id stored within \`ddict\` or 0 if the dictionary is not
a zstd dictionary. If it returns 0 \`ddict\` will be loaded as a
content-only dictionary.

.. _`zstd_getdictid_fromframe`:

ZSTD_getDictID_fromFrame
========================

.. c:function:: unsigned int ZSTD_getDictID_fromFrame(const void *src, size_t srcSize)

    returns the dictionary id stored in a zstd frame

    :param const void \*src:
        Source buffer. It must be a zstd encoded frame.

    :param size_t srcSize:
        The size of the source buffer. It must be at least as large as the
        frame header. \`ZSTD_frameHeaderSize_max\` is always large enough.

.. _`zstd_getdictid_fromframe.return`:

Return
------

The dictionary id required to decompress the frame stored within
\`src\` or 0 if the dictionary id could not be decoded. It can return
0 if the frame does not require a dictionary, the dictionary id
wasn't stored in the frame, \`src\` is not a zstd frame, or \`srcSize\`
is too small.

.. _`zstd_frameparams`:

typedef ZSTD_frameParams
========================

.. c:type:: typedef ZSTD_frameParams

    zstd frame parameters stored in the frame header

.. _`zstd_getframeparams`:

ZSTD_getFrameParams
===================

.. c:function:: size_t ZSTD_getFrameParams(ZSTD_frameParams *fparamsPtr, const void *src, size_t srcSize)

    extracts parameters from a zstd or skippable frame

    :param ZSTD_frameParams \*fparamsPtr:
        On success the frame parameters are written here.

    :param const void \*src:
        The source buffer. It must point to a zstd or skippable frame.

    :param size_t srcSize:
        The size of the source buffer. \`ZSTD_frameHeaderSize_max\` is
        always large enough to succeed.

.. _`zstd_getframeparams.return`:

Return
------

0 on success. If more data is required it returns how many bytes
must be provided to make forward progress. Otherwise it returns
an error, which can be checked using \ :c:func:`ZSTD_isError`\ .

.. This file was automatic generated / don't edit.

