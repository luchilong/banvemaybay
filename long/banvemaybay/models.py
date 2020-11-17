from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Time
from sqlalchemy.orm import relationship
from banvemaybay import db


class Category(db.Model):
    __tablename__ = "Lịch Chuyến Bay"

    MaCB = Column(Integer, primary_key=True, autoincrement=True)
    SBdi = Column(String(50), nullable=True)
    SBden = Column(String(50), nullable=True)
    Day_hour = Column(DateTime(True))
    Timefly = Column(Time(True))
    SlotN = Column(Integer, default=0)
    SlotV = Column(Integer, default=0)
    Product = relationship('Product', backrek="C", lazy=True)


class Product(db.Model):
    __tablename__ = "Vé Chuyến Bay"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    CB = Column(Integer, ForeignKey(Category.MaCB), nullable=False)


class Phieudatcho(db.Model):
    __tablename__ = "Phiếu Đặt Chỗ"

    pass


class DSchuyenbay(db.Model):
    __tablename__ = "Danh Sách Chuyến Bay"

    pass


class Baocaodanhthu(db.Model):
    __tablename__ = "Báo Cao Danh Thu"

    pass


class Danhthunam(db.Model):
    __tablename__ = "Danh Thu Năm"

    pass


if __name__ == '__main__':
    db.create_all()
