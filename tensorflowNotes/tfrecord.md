# tfsample & tfrecord

在 tensorflow 中的一种的格式是 tfsqmple 格式的样本存储。在存储这种格式的样本主要是有三种格式进行存储：

- byte-list：负责的是string类型的数据；
- int-list：整型的数据；
- float-list：浮点型的数据；

```python
feature.SerializeToString()
```

并通过上面的代码转换为二进制文件进行存储；

```python
def serialize_example(feature0, feature1, feature2, feature3):
  """
  Creates a tf.Example message ready to be written to a file.
  """
  # Create a dictionary mapping the feature name to the tf.Example-compatible
  # data type.
  feature = {
      'feature0': _int64_feature(feature0),
      'feature1': _int64_feature(feature1),
      'feature2': _bytes_feature(feature2),
      'feature3': _float_feature(feature3),
  }

  # Create a Features message using tf.train.Example.

  example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
  return example_proto.SerializeToString()
```

上面的函数分别将输入的样本数据（单个样本的每一个维度）进行处理，然后序列化进行存储；

```python
example_proto = tf.train.Example.FromString(serialized_example)
example_proto
```

通过上面的代码可以得到样本的原来的样子

但是这样单条的数据处理不太方面，如果想使用样本的 map 函数：

```python
features_dataset=tf.data.Dataset.from_tensor_slices((feature0, feature1, feature2,feature3))
features_dataset
```

首先将样本的每一个特征组合在一起处理成为此数据集；

然后将上面的 serialize_example 函数进行包装一下：

```python
def tf_serialize_example(f0,f1,f2,f3):
  tf_string = tf.py_function(
    serialize_example,
    (f0,f1,f2,f3),  # pass these args to the above function.
    tf.string)      # the return type is `tf.string`.
  return tf.reshape(tf_string, ()) # The result is a scalar
```

这样就可以将整体的数据进行序列化了：

```python
serialized_features_dataset = features_dataset.map(tf_serialize_example)
serialized_features_dataset
```

可以说这样的数据就是tfrecord格式的数据：

也可以通过 generator 的形式生成数据：

```python
def generator():
  for features in features_dataset:
    yield serialize_example(*features)
```

先建立生成器，每一个数据进行处理，然后生成数据：

```python
serialized_features_dataset = tf.data.Dataset.from_generator(generator,output_types=tf.string,output_shapes=())
```

也可以得到这样的数据，最后将数据写入文件：

```python
filename = 'test.tfrecord'
writer = tf.data.experimental.TFRecordWriter(filename)
writer.write(serialized_features_dataset)
```

