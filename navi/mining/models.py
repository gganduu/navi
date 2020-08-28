from django.db import models

# Create your models here.

class Topology_Type(models.Model):
    TT_id = models.AutoField(primary_key=True)
    TT_type = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = 'Topology_Type'

class Topology(models.Model):
    TOP_id = models.AutoField(primary_key=True)
    TOP_name = models.CharField(max_length=100, null=True, db_index=True)
    TOP_version = models.CharField(max_length=10, null=True)
    TOP_input_shape = models.CharField(max_length=45, null=True)
    TOP_graph = models.BinaryField(null=False)
    TOP_source_url = models.URLField(max_length=250, null=True)
    TOP_cost = models.FloatField(null=False, db_index=True)
    TOP_type = models.ForeignKey(to='Topology_Type', on_delete=models.DO_NOTHING)
    TOP_desc = models.TextField(null=True, default='desc of the topology')
    TOP_png = models.BinaryField(null=False)
    TOP_order = models.IntegerField(null=False, db_index=True)

    class Meta:
        db_table = 'Topology'

class Pattern(models.Model):
    PAT_id = models.AutoField(primary_key=True)
    PAT_key = models.CharField(max_length=4096, null=False, db_index=True, default='the key string of the pattern')
    PAT_graph = models.BinaryField(null=False)
    PAT_order = models.IntegerField(null=False)
    PAT_name = models.CharField(max_length=45, null=True)
    PAT_desc = models.CharField(max_length=4096, null=True)
    PAT_png = models.BinaryField(null=False)

    class Meta:
        db_table = 'Pattern'

class Match_Method_Type(models.Model):
    MMT_id = models.AutoField(primary_key=True)
    MMT_type_desc = models.CharField(max_length=256, null=False)

    class Meta:
        db_table = 'Match_Method_Type'

class Matched(models.Model):
    MAT_id = models.AutoField(primary_key=True)
    MAT_graph = models.BinaryField(null=False)
    MAT_order = models.IntegerField(null=False)
    MAT_pattern = models.ForeignKey(to='Pattern', db_index=True, on_delete=models.DO_NOTHING)
    MAT_cost = models.FloatField(null=False, db_index=True)
    MAT_ideal_cost = models.FloatField(null=False)
    MAT_ideal_cost_saving = models.FloatField(null=False)
    MAT_comment = models.TextField(null=True)
    MAT_png = models.BinaryField(null=False)
    MAT_topology = models.ForeignKey(to='Topology', db_index=True, on_delete=models.DO_NOTHING)
    MAT_match_method_type = models.ForeignKey(to='Match_Method_Type', db_index=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'Matched'

class Key_Type(models.Model):
    KT_id = models.AutoField(primary_key=True)
    KT_key_desc = models.TextField(null=False, default='desc of key type')

    class Meta:
        db_table = 'Key_Type'

class Match_Key(models.Model):
    MK_match = models.ForeignKey(to='Matched', db_index=True, on_delete=models.DO_NOTHING)
    MK_key_type = models.ForeignKey(to='Key_Type', db_index=True, on_delete=models.DO_NOTHING)
    MK_key = models.TextField(null=False)

    class Meta:
        db_table = 'Match_Key'

class Pattern_Source(models.Model):
    PS_pattern = models.ForeignKey(to='Pattern', db_index=True, on_delete=models.DO_NOTHING)
    PS_topology = models.ForeignKey(to='Topology', db_index=True, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'Pattern_Source'
