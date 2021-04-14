import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {Stage, StageRelations} from '../models';

export class StageRepository extends DefaultCrudRepository<
  Stage,
  typeof Stage.prototype.stage_id,
  StageRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(Stage, dataSource);
  }
}
