# $0$ buffersize
# $1$ Messageformat
# $2$ BufferName

$2$: record
  Queue: array[0..$0$] of $1$;
  QueueInd: 0..$0$+1;
end;