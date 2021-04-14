import {inject} from '@loopback/core';
import {DefaultCrudRepository} from '@loopback/repository';
import {EllementoDbDataSource} from '../datasources';
import {LocationStageAssignment, LocationStageAssignmentRelations} from '../models';

export class LocationStageAssignmentRepository extends DefaultCrudRepository<
  LocationStageAssignment,
  typeof LocationStageAssignment.prototype.location_stage_assignment_id,
  LocationStageAssignmentRelations
> {
  constructor(
    @inject('datasources.ellemento_db') dataSource: EllementoDbDataSource,
  ) {
    super(LocationStageAssignment, dataSource);
  }
}
