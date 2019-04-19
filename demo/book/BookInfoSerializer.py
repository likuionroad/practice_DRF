from rest_framework import serializers
from .models import HeroInfo, BookInfo


class BookInfoSerializer(serializers.ModelSerializer):
    """图书数据序列化器"""

    """图书数据序列化器"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)
    heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # 新增

    class Meta:
        model = BookInfo
        # fields = '__all__'
        # 排除调不要的
        exclude = ('is_delete',)

    # 对标题进行校验
    # def validate_btitle(self, value):
    #     if '平凡' not in value:
    #         raise serializers.ValidationError("图书不是关于平凡的世界的")
    #     return value

    def create(self, validated_data):
        """新建"""
        return BookInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """更新，instance为跟新的对象"""
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.save()
        return instance









class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)

    class Meta:
        model = HeroInfo
        # fields = '__all__'
        # 排除调不要的
        exclude = ('is_delete',)
